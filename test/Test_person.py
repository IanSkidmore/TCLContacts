# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:33:12 2016

@author: IAN
"""

import unittest
import datetime

from person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.Person = Person('Adam','Skidmore')
        
    def tearDown(self):
        self.Person = None
        
    def test_initialisation(self):
        p = Person('Ian','Skidmore')     
        self.assertEqual(p.Forename,'Ian')
        self.assertEqual(p.Surname,'Skidmore')
        
    def test_age_calculation(self):
        p = Person('Ian','Skidmore')
        p.DateOfBirth = datetime.date(1964,9,29)
        self.assertEqual(p.Age(),51)
        
        p = Person('Adam','Skidmore')
        p.DateOfBirth = datetime.date(2002,2,18)
        self.assertEqual(p.Age(),14)       
        
    def test_age_calculation_leap_year(self):
        p = Person('Adam','Skidmore')
        p.DateOfBirth = datetime.date(2000,2,29)
        self.assertEqual(p.Age(),16)    

    def test_has_mobile_phone(self):
        self.assertFalse(self.Person.HasMobilePhone())
        self.Person.MobilePhoneNumber = '07abcde'
        self.assertFalse(self.Person.HasMobilePhone())        
        self.Person.MobilePhoneNumber = '07789955357'
        self.assertTrue(self.Person.HasMobilePhone())
        self.Person.MobilePhoneNumber = '01159724441'
        self.assertFalse(self.Person.HasMobilePhone())       
        
    def test_has_landline_phone(self):
        self.assertFalse(self.Person.HasLandlinePhone())
        self.Person.LandlinePhoneNumber = '07789955357'
        self.assertFalse(self.Person.HasLandlinePhone())
        self.Person.LandlinePhoneNumber = '0115abcde'
        self.assertFalse(self.Person.HasLandlinePhone())  
        self.Person.LandlinePhoneNumber = '03459724441'
        self.assertFalse(self.Person.HasLandlinePhone())
        self.Person.LandlinePhoneNumber = '01159724441'
        self.assertTrue(self.Person.HasLandlinePhone())          
        
    def test_has_phone(self):
        self.assertFalse(self.Person.HasPhone())
        self.Person.LandlinePhoneNumber = '07789955357'
        self.assertFalse(self.Person.HasPhone())
        self.Person.LandlinePhoneNumber = '01159724441'
        self.assertTrue(self.Person.HasPhone())   
        self.Person.LandlinePhoneNumber = None
        self.assertFalse(self.Person.HasPhone())   
        self.Person.MobilePhoneNumber = '07789955357'
        self.assertTrue(self.Person.HasPhone())
        self.Person.MobilePhoneNumber = '01159724441'
        self.assertFalse(self.Person.HasPhone())          
        
    def test_has_email(self):
        self.assertFalse(self.Person.HasEmailAddress())        
        self.Person.EmailAddress = 'This is a fake emailaddress'
        self.assertFalse(self.Person.HasEmailAddress())
        self.Person.EmailAddress = 'adam.skidmore@btinternet.com'
        self.assertTrue(self.Person.HasEmailAddress())        
    