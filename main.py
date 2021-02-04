# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:39:39 2020

@author: Nabeel
"""
import os
import sys
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
import pyqtgraph as pg
from layout import Ui_MainWindow
from dialog_layout import Ui_Dialog
from email_layout import Ui_Mail_Dialog
from budget_layout import Ui_Budget_Dialog
from expense_model import ExpenseModel as EM
from expense_model import Expense
from budget_model import Budget
from db import *

USER_FILE = 'User.db'


class Window(QMainWindow):
    """The window display class for the application."""
    def __init__(self):
        """Initializing important attributes."""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.forward.clicked.connect(self.next_page)
        self.ui.backward.clicked.connect(self.prev_page)
        self.ui.add.clicked.connect(self.add)
        self.ui.delete.clicked.connect(self.delete)
        self.ui.update.clicked.connect(self.update)

        self.ui.actionCsv.triggered.connect(self.open_csv)
        self.ui.actionExcel.triggered.connect(self.open_xl)
        self.ui.actionMail_Report.triggered.connect(self.send_report)
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionAdd_Balance.triggered.connect(self.add_bg)
        self.ui.actionUpdate_Balance.triggered.connect(self.add_bg)
        self.plot_data = 0
        self.plot_chart()

        self.budget = 0
        self.budget_data = []
        self.expended_list = []
        self.model = EM()
        self.ui.listView_1.setModel(self.model)
        self.load()

        self.update_bg()
        self.update_exp()
        self.update_page_3()

    def next_page(self):
        """Goes to the next page of the list view"""
        self.ui.stackedWidget.setCurrentIndex(
            self.ui.stackedWidget.currentIndex()+1)

    def prev_page(self):
        """Goes to the previous page of the list view"""
        self.ui.stackedWidget.setCurrentIndex(
            self.ui.stackedWidget.currentIndex()-1)

    def add(self):
        """Adds new Expense object to the list"""
        self.dialog = QDialog()
        self.dialog.ui = Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        if self.dialog.exec_():
            date = self.dialog.ui.dateEdit.date().toPyDate()
            category = self.dialog.ui.comboBox.currentText()
            sub = self.dialog.ui.comboBox_2.currentText()
            exp = self.dialog.ui.doubleSpinBox.value()
            x = Expense(date, category, sub, exp)
            self.model.data.append(x)
            self.model.layoutChanged.emit()
            self.save()
            self.update_bg()
            self.update_exp()
            self.update_page_3()
            self.update_chart()

    def update(self):
        """Updates the selected Expense object."""
        all_attributes = ['category', 'subcategory', 'cost', 'date']
        indexes = self.ui.listView_1.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            element = self.model.data[row]
            self.dialog = QDialog()
            self.dialog.ui = Ui_Dialog()
            self.dialog.ui.setupUi(self.dialog)
            date = datetime.datetime.strptime(str(element.date), "%Y-%m-%d")
            self.dialog.ui.dateEdit.setDate(date)
            self.dialog.ui.doubleSpinBox.setValue(element.cost)

            i = self.dialog.ui.comboBox.findText(element.category)
            if i >= 0:
                self.dialog.ui.comboBox.setCurrentIndex(i)
            i = self.dialog.ui.comboBox_2.findText(element.subcategory)
            if i >= 0:
                self.dialog.ui.comboBox_2.setCurrentIndex(i)
            rowid = find_id(element)[0]
            if self.dialog.exec_():
                date = self.dialog.ui.dateEdit.date().toPyDate()
                category = self.dialog.ui.comboBox.currentText()
                sub = self.dialog.ui.comboBox_2.currentText()
                cost = self.dialog.ui.doubleSpinBox.value()
                self.model.data[row] = Expense(date, category, sub, cost)
                for i in all_attributes:
                    update_expense(self.model.data[row], rowid, i)
                self.model.dataChanged.emit(index, index)
                self.save()
                self.update_bg()
                self.update_exp()
                self.update_page_3()
                self.update_chart()
        self.ui.listView_1.clearSelection()

    def delete(self):
        """Deletes the selected Expense object."""
        indexes = self.ui.listView_1.selectedIndexes()
        if indexes:
            index = indexes[0]
            rowid = find_id(self.model.data[index.row()])[0]
            delete_expense(str(rowid))
            del self.model.data[index.row()]
            self.model.layoutChanged.emit()
            self.ui.listView_1.clearSelection()
            self.save()
            self.update_bg()
            self.update_exp()
            self.update_page_3()
            self.update_chart()

    def load(self):
        """Loads all the Expense objects in the USER_FILE."""
        for i in get_expenses():
            x = Expense(i[1], i[2], i[3], i[4])
            if i[1] not in self.expended_list:
                self.expended_list.append(i[1])
            self.model.data.append(x)
        self.model.layoutChanged.emit()
        for i in get_budgets():
            tmp = Budget(i[1], i[2])
            self.budget_data.append(tmp)
        for i in self.budget_data:
            self.budget += i.cost

    def save(self):
        """Saves Expense objects on the USER_FILE."""
        for i in self.model.data:
            if find_id(i) is None:
                add_expense(i)

    def get_total_expense(self):
        """Returns the total expenses."""
        expenses = []
        for i in self.model.data:
            expenses.append(i.cost)
        return sum(expenses)

    def get_total_budget(self):
        """Returns the total budget."""
        budget = []
        for i in self.budget_data:
            budget.append(i.cost)
        return sum(budget)

    def plot_chart(self):
        """Plots the chart"""
        try:
            x = []
            for i in get_expenses():
                x.append(i[4])
            pen = pg.mkPen(color='r', width=3)
            self.ui.widget.addLegend(offset=(-30,10))
            self.plot_data = self.ui.widget.plot(x, name='Expenses', pen=pen,
                                                 symbol='o')
            y = []
            for i in get_budgets():
                y.append(i[1])
            pen = pg.mkPen(color='y', width=3)
            self.plot_budget = self.ui.widget.plot(y, name='Budgets', pen=pen,
                                                 symbol='s')
            self.ui.widget.setTitle("Expense Track", color='#ffffff',
                                    size='14pt')
            styles = {'font-size':'12pt'}
            self.ui.widget.setLabel("left", 'Expense', color='#ffffff', **styles)
            self.ui.widget.setLabel("bottom","Days",color='#ffffff',
                                    **styles)
        except FileNotFoundError:
            pass

    def update_chart(self):
        """Updates the chart when a budget or expense is changed."""
        x = []
        for i in get_expenses():
            x.append(i[4])
        self.plot_data.setData(x)
        y = []
        for i in get_budgets():
            y.append(i[1])
        self.plot_budget.setData(y)

    def send_report(self):
        """Sends email to the given mail."""
        self.emaildialog = QDialog()
        self.emaildialog.ui = Ui_Mail_Dialog()
        self.emaildialog.ui.setupUi(self.emaildialog)
        if self.emaildialog.exec_():
            email = self.emaildialog.ui.email.text()
            body = f"""<hr></hr>
<h4>Dear {self.emaildialog.ui.username.text()},</h4>
Following is your budget & expense report<br>
&nbsp;&nbsp;&nbsp;&nbsp;<b>expenses:</b> {self.ui.expense_dsp.text()}<br>
&nbsp;&nbsp;&nbsp;&nbsp;<b>current balance:</b> {self.ui.crt_balance.text()}<br>
&nbsp;&nbsp;&nbsp;&nbsp;<b>budget avg (daily):</b> {self.ui.daily_avg.text()}<br>
&nbsp;&nbsp;&nbsp;&nbsp;<b>budget avg (monthly):</b> {self.ui.monthly_avg.text()}<br>
&nbsp;&nbsp;&nbsp;&nbsp;<b>Total budget:</b> Rs {self.get_total_budget()}/-<br>
<hr></hr>"""
            try:
                smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
                smtpObj.ehlo()
                smtpObj.starttls()
                smtpObj.login('xxxxxxxxxxxxxxxxx', 'xxxxxxxxx')
                msg = MIMEMultipart('alternative')
                msg['Subject'] = 'Budget & Expense report'
                text_part = MIMEText('Hello!', 'plain')
                body_part = MIMEText(body, 'html')
                msg.attach(text_part)
                msg.attach(body_part)
                # msg = "Subject: Expense report\n\n{}".format(body)
                check = smtpObj.sendmail('xxxxxxxxxxxxxxxxxxxxxxxxxx',
                                     email, msg.as_string())
                smtpObj.quit()
                if check != {}:
                    raise Exception
            except Exception:
                msg = QMessageBox()
                msg.setWindowTitle("Expense Tracker")
                msg.setWindowIcon(QtGui.QIcon("icon.png"))
                msg.setText("Not connected to internet!\nCheck your connection and retry.")
                tmp = msg.exec_()
                
            

    def open_csv(self):
        """Opens the USER_FILE in MS Excel"""
        name, extension = os.path.splitext(USER_FILE)
        xl_file = name+".csv"
        data_dict = {}
        for i in self.model.data:
            if data_dict.get('date') is None:
                data_dict['date'] = [i.date]
            else:
                data_dict['date'].append(i.date)
            if data_dict.get('category') is None:
                data_dict['category'] = [i.category]
            else:
                data_dict['category'].append(i.category)
            if data_dict.get('subcategory') is None:
                data_dict['subcategory'] = [i.subcategory]
            else:
                data_dict['subcategory'].append(i.subcategory)
            if data_dict.get('cost') is None:
                data_dict['cost'] = [i.cost]
            else:
                data_dict['cost'].append(i.cost)
        df = pd.DataFrame(data_dict)
        df.to_csv(xl_file, index=False)
        os.startfile(xl_file)

    def open_xl(self):
        """Generates an excel file and opens it in MS Excel."""
        name, extension = os.path.splitext(USER_FILE)
        xl_file = name+".xlsx"
        data_dict = {}
        for i in self.model.data:
            if data_dict.get('date') is None:
                data_dict['date'] = [i.date]
            else:
                data_dict['date'].append(i.date)
            if data_dict.get('category') is None:
                data_dict['category'] = [i.category]
            else:
                data_dict['category'].append(i.category)
            if data_dict.get('subcategory') is None:
                data_dict['subcategory'] = [i.subcategory]
            else:
                data_dict['subcategory'].append(i.subcategory)
            if data_dict.get('cost') is None:
                data_dict['cost'] = [i.cost]
            else:
                data_dict['cost'].append(i.cost)
        df = pd.DataFrame(data_dict)
        df.to_excel(xl_file, index=False)
        os.startfile(xl_file)

    def add_bg(self):
        """Adds budget."""
        self.dialog = QDialog()
        self.dialog.ui = Ui_Budget_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        if self.dialog.exec_():
            value = self.dialog.ui.amount.value()
            if value == 0:
                return
            date = self.dialog.ui.daily_date_edit.date().toPyDate()
            tmp = Budget(value, date)
            x = find_budget_by_date(tmp)
            if x is None:
                add_budget(tmp)
                self.budget_data.append(tmp)
            else:
                first = x[0]
                new_cost = x[1] + value
                tmp_budget = Budget(new_cost, date)
                update_budget(tmp_budget, first, 'cost')
                for i in range(len(self.budget_data)):
                    tmp_date = self.budget_data[i].date
                    if tmp_date == date:
                        del self.budget_data[i]
            self.budget += value
            self.update_chart()
            self.update_bg()
            self.update_exp()
            self.update_page_3()

    def update_bg(self):
        """Updates the budget on page 3."""
        days = len(get_budgets())
        if days == 0:
            budget_avg = 0.0
        else:
            budget_avg = self.get_total_budget() / days
        self.ui.budget_avg.setText(f'Rs: {round(budget_avg,2)}/-')
        self.ui.budget_monthly_avg.setText(f'Rs: {round(budget_avg*30,2)}/-')
        self.ui.actual_budget_avg.setText(f'Rs: {self.get_total_budget()}/-')

    def update_exp(self):
        """Updates the current expenses."""
        self.ui.expense_dsp.setText(
            f"Rs: {round(self.get_total_expense(),2)}/-")

    def update_page_3(self):
        """"Updates all the data on page 3."""
        total_days = len(self.expended_list)
        if total_days == 0 and self.budget != 0:
            total_days = len(self.budget_data)
        self.ui.crt_balance.setText(
            f"Rs: {round(self.budget*total_days - self.get_total_expense(),2)}/-")
        self.ui.balance_dsp.setText(
            f"Rs: {round(self.budget*total_days - self.get_total_expense(),2)}/-")
        if total_days != 0:
            self.ui.daily_avg.setText(
                f"Rs: {round(self.get_total_expense()/total_days,2)}/-")
            self.ui.monthly_avg.setText(
                f"Rs: {round(self.get_total_expense()/total_days *30,2)}/-")
        else:
            self.ui.daily_avg.setText(f"Rs: 0/-")
            self.ui.monthly_avg.setText(f"Rs: 0/-")


if __name__ == "__main__":
    app = QApplication([])
    w = Window()
    w.show()
    app.exec_()
    sys.exit()
