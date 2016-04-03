# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 18:12:40 2016

@author: IAN
"""
import json

class Organisation():
    def __init__(self,n=''):
        self.Name = n
        self.SupplierFlag = False
        self.ClientFlag = False
        
    def IsSupplier(self):
        return self.SupplierFlag

    def IsClient(self):
        return self.ClientFlag        
        
    def to_JSON(self):
        return json.dumps(self.__dict__)
        
    def LoadFromJSON(self,s):        
        o = json.loads(s)
        self.Name = o['Name']
        self.SupplierFlag = o['SupplierFlag']
        self.ClientFlag = o['ClientFlag']      
     