# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 16:35:40 2016

@author: IAN
"""
import json

class Country():
    def __init__(self,n=''):
        self.Name = n
        
    def to_JSON(self):
        d = dict(Name=self.Name)
        return json.dumps(d)
        
    def LoadFromJSON(self,s):        
        o = json.loads(s)
        self.Name = o['Name']   