# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 16:41:23 2016

@author: IAN
"""

import unittest

from address import Address
from country import Country

class TestAddress(unittest.TestCase):
    def setUp(self):
        self.Address = Address('Barrack Lane','Nottingham')
        self.Address.HouseNumber = '1'
        self.Address.PostCode = 'NG7 9AN'
        
    def tearDown(self):
        self.Address = None
        
    def test_address_initialisation(self):
        self.assertEqual(self.Address.StreetName, 'Barrack Lane')
        self.assertEqual(self.Address.Town, 'Nottingham')
        self.assertEqual(self.Address.Country, None)
        self.assertFalse(self.Address.IsPAFValidated())
        
    def test_paf_validation(self):
        self.assertFalse(self.Address.IsPAFValidated())        
        self.Address.SetPAFValidated()
        self.assertTrue(self.Address.IsPAFValidated())        
        
    def test_address_line_1_house_number(self):
        self.assertEqual(self.Address.AddressLine1(),'1, Barrack Lane')
        self.assertEqual(self.Address.AddressLine2(), None)
        self.assertEqual(self.Address.AddressLine3(), None) 
        self.assertEqual(self.Address.AddressLine4(), None) 
        
    def test_address_line_1_house_name(self):        
        self.Address.HouseName = 'Maitland Flats'
        self.assertEqual(self.Address.AddressLine1(),'Maitland Flats, Barrack Lane')
        self.assertEqual(self.Address.AddressLine2(), None)   
        self.assertEqual(self.Address.AddressLine3(), None)
        self.assertEqual(self.Address.AddressLine4(), None) 
        
    def test_address_line_1_flat_name(self):        
        self.Address.FlatName = 'Flat 5'    
        self.assertEqual(self.Address.AddressLine1(),'Flat 5, 1 Barrack Lane')
        self.assertEqual(self.Address.AddressLine2(), None) 
        self.assertEqual(self.Address.AddressLine3(), None) 
        self.assertEqual(self.Address.AddressLine4(), None) 
        
    def test_address_line_1_flat_name_house_name(self):        
        self.Address.FlatName = 'Flat 5'    
        self.Address.HouseName = 'Maitland Flats'        
        self.assertEqual(self.Address.AddressLine1(),'Flat 5, Maitland Flats')
        self.assertEqual(self.Address.AddressLine2(),'1, Barrack Lane') 
        self.assertEqual(self.Address.AddressLine3(), None) 
        self.assertEqual(self.Address.AddressLine4(), None) 
        
    def test_address_line_2_house_number_locality(self):
        self.Address.LocalityName = 'Lenton'
        self.assertEqual(self.Address.AddressLine1(),'1, Barrack Lane')
        self.assertEqual(self.Address.AddressLine2(), 'Lenton')
        self.assertEqual(self.Address.AddressLine3(), None)
        self.assertEqual(self.Address.AddressLine4(), None) 

    def test_address_line_2_house_name_locality(self):        
        self.Address.HouseName = 'Maitland Flats'
        self.Address.LocalityName = 'Lenton'        
        self.assertEqual(self.Address.AddressLine1(),'Maitland Flats, Barrack Lane')
        self.assertEqual(self.Address.AddressLine2(), 'Lenton')  
        self.assertEqual(self.Address.AddressLine3(), None)   
        self.assertEqual(self.Address.AddressLine4(), None)         
        
    def test_address_line_2_flat_name_locality(self):
        self.Address.FlatName = 'Flat 5' 
        self.Address.LocalityName = 'Lenton'          
        self.assertEqual(self.Address.AddressLine1(),'Flat 5, 1 Barrack Lane')
        self.assertEqual(self.Address.AddressLine2(),'Lenton')   
        self.assertEqual(self.Address.AddressLine3(), None)         
        self.assertEqual(self.Address.AddressLine4(), None)      
        
    def test_address_line_2_flat_name_house_name_locality(self):        
        self.Address.FlatName = 'Flat 5'    
        self.Address.HouseName = 'Maitland Flats' 
        self.Address.LocalityName = 'Lenton'           
        self.assertEqual(self.Address.AddressLine1(),'Flat 5, Maitland Flats')
        self.assertEqual(self.Address.AddressLine2(),'1, Barrack Lane') 
        self.assertEqual(self.Address.AddressLine3(), 'Lenton') 
        self.assertEqual(self.Address.AddressLine4(), None)         
        
    def test_country_allocation(self):
        self.Address.Country = Country('United Kingdom')
        self.assertEqual(self.Address.Country.Name, 'United Kingdom')        