# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'budget_layout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Budget_Dialog(object):
    def setupUi(self, Dialog):
        self.monthly_flag = False
        self.daily_flag= False
        Dialog.setObjectName("Dialog")
        Dialog.resize(414, 288)
        Dialog.setWindowIcon(QtGui.QIcon("icon.png"))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(120, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        # self.monthly_check = QtWidgets.QRadioButton(Dialog)
        # self.monthly_check.setGeometry(QtCore.QRect(40, 60, 82, 17))
        # self.monthly_check.setObjectName("monthly_check")
        # self.daily_check = QtWidgets.QRadioButton(Dialog)
        # self.daily_check.setGeometry(QtCore.QRect(40, 90, 82, 17))
        # self.daily_check.setObjectName("daily_check")
        self.date_label = QtWidgets.QLabel(Dialog)
        self.date_label.setGeometry(QtCore.QRect(40, 90, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.date_label.setFont(font)
        self.date_label.setText("Date:")
        self.amount_label = QtWidgets.QLabel(Dialog)
        self.amount_label.setGeometry(QtCore.QRect(40, 160, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.amount_label.setFont(font)
        self.amount_label.setObjectName("amount_label")
        self.amount = QtWidgets.QDoubleSpinBox(Dialog)
        self.amount.setGeometry(QtCore.QRect(110, 160, 251, 22))
        self.amount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.amount.setObjectName("amount")
        self.amount.setMaximum(999999999999999999)
        self.amount.setMinimum(-999999999999999999)
        self.daily_date_edit = QtWidgets.QDateEdit(Dialog)
        self.daily_date_edit.setGeometry(QtCore.QRect(140, 90, 110, 22))
        self.daily_date_edit.setCalendarPopup(True)
        self.daily_date_edit.setObjectName("daily_date_edit")
        date = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")
        self.daily_date_edit.setDate(date)
        # self.daily_date_edit.setEnabled(False)
        # self.monthly_date_edit = QtWidgets.QDateEdit(Dialog)
        # self.monthly_date_edit.setGeometry(QtCore.QRect(140, 60, 110, 22))
        # self.monthly_date_edit.setCalendarPopup(True)
        # self.monthly_date_edit.setObjectName("monthly_date_edit")
        # date = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")
        # self.monthly_date_edit.setDate(date)
        # self.monthly_date_edit.setEnabled(False)
        
        # self.monthly_check.toggled.connect(self.change_monthly)
        # self.daily_check.toggled.connect(self.change_daily)
        
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    # def change_monthly(self):
    #     if not self.monthly_flag:
    #         self.monthly_date_edit.setEnabled(True)
    #         self.monthly_flag = True
    #     else:
    #         self.monthly_date_edit.setEnabled(False)
    #         self.monthly_flag = False
        
    # def change_daily(self):
    #     if not self.daily_flag:
    #         self.daily_date_edit.setEnabled(True)
    #         self.daily_flag = True
    #     else:
    #         self.daily_date_edit.setEnabled(False)
    #         self.daily_flag = False

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "Add Budget"))
        # self.monthly_check.setText(_translate("Dialog", "Month"))
        # self.daily_check.setText(_translate("Dialog", "Day"))
        self.amount_label.setText(_translate("Dialog", "Amount:"))
        self.amount.setPrefix(_translate("Dialog", "Rs "))
        self.amount.setSuffix(_translate("Dialog", "/-"))
        self.daily_date_edit.setDisplayFormat(_translate("Dialog", "M/d/yyyy"))
        # self.monthly_date_edit.setDisplayFormat(_translate("Dialog", "M/yyyy"))
        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Budget_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

