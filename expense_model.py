# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:09:23 2020

@author: Nabeel
"""
from PyQt5 import QtCore, QtGui

class ExpenseModel(QtCore.QAbstractListModel):
    def __init__(self, data=None):
        """
        data would be a list of expense objects, each 4 element long
        1st would be date
        2nd would be Category
        3rd would be sub-category
        4th would be expense
        """
        super().__init__()
        if data == None:
            self.data = []
        else:
            self.data = data
            
    def data(self, index, role):
        if role == QtCore.Qt.DecorationRole:
            row = index.row()
            if self.data[row].category == 'Life':
                icon = QtGui.QImage('life.png')
                return icon
            if self.data[row].category == 'Living':
                icon = QtGui.QImage('living.png')
                return icon
            if self.data[row].category == 'Transportation':
                icon = QtGui.QImage('transportation.png')
                return icon
            if self.data[row].category == 'Vehicle':
                icon = QtGui.QImage('vehicle.png')
                return icon
            if self.data[row].category == 'Education':
                icon = QtGui.QImage('education.png')
                return icon
            if self.data[row].category == 'Others':
                icon = QtGui.QImage('others.png')
                return icon
            
        if role == QtCore.Qt.DisplayRole:
            packet = self.data[index.row()]
            text = "Category: " + packet.category + "\n"
            text += "Sub-Category: " +  packet.subcategory + "\n"
            text += "Expense: Rs {}/-\n".format(round(packet.cost,2))
            text += "Date: {}\n".format(packet.date)
            text += "_"*75
            return text
        
    def rowCount(self, index):
        if self.data != None:
            return len(self.data)
        
    def __str__(self):
        text =  f"Expense("
        for i in self.data:
            text += str(i)
        text += ')'
        return text
        
class Expense:
    def __init__(self, date, cat, sub, cost):
        self.date = date
        self.category = cat
        self.subcategory = sub
        self.cost = cost
        
    def __str__(self):
        return f"{self.date}, {self.category}, {self.subcategory}, {self.cost}"