# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'email_layout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
# expensetracker666@gmail.com
import re
from PyQt5 import QtCore, QtGui, QtWidgets

def validate_email(email):
    emailReg = re.compile(r"([a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))",re.VERBOSE)
    if emailReg.match(email):
        return True
    return False

class Ui_Mail_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(381, 292)
        Dialog.setWindowIcon(QtGui.QIcon("icon.png"))
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 140, 321, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.usr_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.usr_label.setFont(font)
        self.usr_label.setObjectName("usr_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usr_label)
        self.username = QtWidgets.QLineEdit(self.layoutWidget)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        self.email_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.email_label)
        self.email = QtWidgets.QLineEdit(self.layoutWidget)
        self.email.setObjectName("email")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.email)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 30, 231, 101))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.mail_report = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.mail_report.setFont(font)
        self.mail_report.setAlignment(QtCore.Qt.AlignCenter)
        self.mail_report.setObjectName("mail_report")
        self.verticalLayout.addWidget(self.mail_report)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 220, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(lambda:self.check_email(Dialog))
        self.buttonBox.rejected.connect(Dialog.reject)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Expense Tracker"))
        self.usr_label.setText(_translate("Dialog", "User name:"))
        self.email_label.setText(_translate("Dialog", "Email:"))
        self.title.setText(_translate("Dialog", "Expense Tracker"))
        self.mail_report.setText(_translate("Dialog", "mail report"))

    def check_email(self,Dialog):
        if validate_email(self.email.text()):
            Dialog.accept()
        else:
            if self.email.text() == "":
                self.mail_report.setText("Please enter an email address.")
            else:
                self.mail_report.setText("Incorrect email address.")
            self.mail_report.adjustSize()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Mail_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

