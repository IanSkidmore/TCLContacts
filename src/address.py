# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 16:41:06 2016

@author: IAN
"""
import datetime

class Address():
    def __init__(self,s,t):
        self.StreetName = s
        self.Town = t
        self.Country = None
        self.PAFValidationDate = None
        self.FlatName = None
        self.HouseName = None
        self.HouseNumber = None
        self.LocalityName = None
        self.County = None
        self.PostCode = None
        self.AddressLines = []
        
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
        
        