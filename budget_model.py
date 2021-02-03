# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 20:42:27 2020

@author: Nabeel
"""
class Budget:
    def __init__(self, cost, date):
        self.cost = float(cost) 
        self.date = date
        
    def __repr__(self):
        return f'Budget({self.cost}, {self.date})'