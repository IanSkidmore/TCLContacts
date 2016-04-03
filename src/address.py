# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 16:41:06 2016

@author: IAN
"""
import datetime
import json
from country import Country

class Address():
    def __init__(self,s='',t=''):
        self.StreetName = s
        self.Town = t
        self.Country = Country()
        self.PAFValidationDate = None
        self.FlatName = None
        self.HouseName = None
        self.HouseNumber = None
        self.LocalityName = None
        self.County = None
        self.PostCode = None
        self.AddressLines = []
    
    def _complexHandler(self, Obj):
        if hasattr(Obj, 'to_JSON'):
            return Obj.to_JSON()
        else:
            raise TypeError, 'Object of type %s with value of %s is not JSON serializable' % (type(Obj), repr(Obj))
        
    def to_JSON(self):
        return json.dumps(self.__dict__, default=self._complexHandler)
        
    def LoadFromJSON(self,s):        
        o = json.loads(s)
        self.StreetName = o['StreetName']  
        self.Town = o['Town']  
        self.Country.LoadFromJSON(o['Country'])  
        self.PAFValidationDate = o['PAFValidationDate']  
        self.FlatName = o['FlatName']  
        self.HouseName = o['HouseName']  
        self.HouseNumber = o['HouseNumber']  
        self.LocalityName = o['LocalityName']  
        self.County = o['County']  
        self.PostCode = o['PostCode']  
        self.AddressLines = o['AddressLines']  
        
    def IsPAFValidated(self):
        return self.PAFValidationDate is not None
        
    def SetPAFValidated(self):
        self.PAFValidationDate = datetime.date.today()
        
    def _setAddressLines(self):
        # deal with flat name
        if self.FlatName is not None:
            res = self.FlatName
            if self.HouseName is not None:
                res += ', ' + self.HouseName
                self.AddressLines.append(res)
                self.AddressLines.append(self.HouseNumber + ', ' + self.StreetName)
                if self.LocalityName is not None:
                    self.AddressLines.append(self.LocalityName)
            else:
                res += ', ' + self.HouseNumber + ' ' + self.StreetName
                self.AddressLines.append(res)
                if self.LocalityName is not None:
                    self.AddressLines.append(self.LocalityName)
        # no flat name, but house name
        elif self.HouseName is not None:
            res = self.HouseName + ', ' + self.StreetName
            self.AddressLines.append(res)
            if self.LocalityName is not None:
                self.AddressLines.append(self.LocalityName)
        # standard address format
        else:
            self.AddressLines.append(self.HouseNumber + ', ' + self.StreetName)
            if self.LocalityName is not None:
                self.AddressLines.append(self.LocalityName)
        
    def AddressLine1(self):
        if len(self.AddressLines) == 0:
            self._setAddressLines()
        return self.AddressLines[0]
        
    def AddressLine2(self):
        if len(self.AddressLines) == 0:
            self._setAddressLines()
        if len(self.AddressLines) > 1:
            return self.AddressLines[1]
        else:
            return None

    def AddressLine3(self):
        if len(self.AddressLines) == 0:
            self._setAddressLines()
        if len(self.AddressLines) > 2:
            return self.AddressLines[2]
        else:
            return None             

    def AddressLine4(self):
        if len(self.AddressLines) == 0:
            self._setAddressLines()
        if len(self.AddressLines) > 3:
            return self.AddressLines[3]
        else:
            return None                 
        
        