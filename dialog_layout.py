# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_layout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets

cat_sub = {'Life':['Food','Clothing/Cosmetics','Health'],
           'Living':['Bills','Furniture','Appliances','Rent'],
           'Transportation':['Bus Travel','Air Travel','Taxi fares'],
           'Vehicle':['Car','Maintenance','Bike','Petrol/Gas'],
           'Education':['Fee','Books','Stationary/Tools'],
           'Others':['Parties','Friends & Family']}

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 259)
        Dialog.setWindowIcon(QtGui.QIcon("icon.png"))
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(120, 20, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 200, 156, 23))
        qtb = QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok
        self.buttonBox.setStandardButtons(qtb)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(50, 69, 321, 121))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.cat_label = QtWidgets.QLabel(self.widget)
        self.cat_label.setObjectName("cat_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.cat_label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.sub_label = QtWidgets.QLabel(self.widget)
        self.sub_label.setObjectName("sub_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sub_label)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.exp_label = QtWidgets.QLabel(self.widget)
        self.exp_label.setObjectName("exp_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.exp_label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox.setProperty("showGroupSeparator", False)
        self.doubleSpinBox.setMaximum(1e+30)
        self.doubleSpinBox.setSingleStep(1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(date.today())
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        for i in cat_sub.keys():
            self.comboBox.addItem(i)
        self.comboBox.currentIndexChanged.connect(self.set_items)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Expense Tracker"))
        self.title.setText(_translate("Dialog", "Add new expense"))
        self.cat_label.setText(_translate("Dialog", "Category:"))
        self.comboBox.setItemText(0, _translate("Dialog", "Category"))
        self.sub_label.setText(_translate("Dialog", "Sub-category:"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Sub-category"))
        self.exp_label.setText(_translate("Dialog", "Expense:"))
        self.doubleSpinBox.setPrefix(_translate("Dialog", "Rs "))
        self.doubleSpinBox.setSuffix(_translate("Dialog", "/-"))
        self.label.setText(_translate("Dialog", "Date:"))
        self.dateEdit.setDisplayFormat(_translate("Dialog", "d/M/yyyy"))

    def set_items(self):
        self.comboBox_2.clear()
        if self.comboBox.currentText() == 'Life':
            for i in cat_sub['Life']:
                self.comboBox_2.addItem(i)
        if self.comboBox.currentText() == 'Living':
            for i in cat_sub['Living']:
                self.comboBox_2.addItem(i)
        if self.comboBox.currentText() == 'Transportation':
            for i in cat_sub['Transportation']:
                self.comboBox_2.addItem(i)
        if self.comboBox.currentText() == 'Vehicle':
            for i in cat_sub['Vehicle']:
                self.comboBox_2.addItem(i)
        if self.comboBox.currentText() == 'Education':
            for i in cat_sub['Education']:
                self.comboBox_2.addItem(i)
        if self.comboBox.currentText() == 'Others':
            for i in cat_sub['Others']:
                self.comboBox_2.addItem(i)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

