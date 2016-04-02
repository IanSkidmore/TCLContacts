# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:39:56 2016

@author: IAN
"""
from datetime import date

class Person():
    
    def __init__(self,f,s):
        self.Forename = f
        self.Surname = s
        
    def AgeOnDate(self, theDay):
        try: 
            birthday = self.DateOfBirth.replace(year=theDay.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday = self.DateOfBirth.replace(year=theDay.year, month=self.DateOfBirth.month+1, day=1)
        return theDay.year - self.DateOfBirth.year - (birthday > theDay)
        
    def Age(self):
        return self.AgeOnDate(date.today())
            
    def HasMobilePhone(self):
        try:
            return self.MobilePhoneNumber is not None and \
            self.MobilePhoneNumber.isdigit() and \
            self.MobilePhoneNumber[0:2] == '07'
        except AttributeError:
            return False
        
    def HasLandlinePhone(self):
        try:
            return self.LandlinePhoneNumber is not None and \
            self.LandlinePhoneNumber.isdigit() and \
            (self.LandlinePhoneNumber[0:2] == '01' or self.LandlinePhoneNumber[0:2] == '02')
        except AttributeError:
            return False   
            
    def HasPhone(self):
        return self.HasLandlinePhone() or self.HasMobilePhone()
        
    def HasEmailAddress(self):
        import re
        EMAIL_REGEX = '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,63}$'
        try:
            return re.match(EMAIL_REGEX, self.EmailAddress) is not None
        except AttributeError:
            return False        
        