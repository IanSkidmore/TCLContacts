# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 18:12:40 2016

@author: IAN
"""

class Organisation():
    def __init__(self,n):
        self.Name = n
        self.SupplierFlag = False
        self.ClientFlag = False
        
    def IsSupplier(self):
        return self.SupplierFlag

    def IsClient(self):
        return self.ClientFlag        