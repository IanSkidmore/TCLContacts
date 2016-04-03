# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 18:13:00 2016

@author: IAN
"""

import unittest

from organisation import Organisation
from address import Address
from country import Country

class TestOrganisation(unittest.TestCase):
    def setUp(self):
        self.Organisation = Organisation('Thorneycreek Consulting Ltd')
        
    def tearDown(self):
        self.Organisation = None
        
    def test_organisation_initialisation(self):
        self.assertEqual(self.Organisation.Name, 'Thorneycreek Consulting Ltd')
        self.assertFalse(self.Organisation.IsClient())
        self.assertFalse(self.Organisation.IsSupplier())

    def test_client_flag_set(self):
        self.assertFalse(self.Organisation.IsClient())
        self.Organisation.ClientFlag = True        
        self.assertTrue(self.Organisation.IsClient())        
        
    def test_supplier_flag_set(self):
        self.assertFalse(self.Organisation.IsSupplier())
        self.Organisation.SupplierFlag = True        
        self.assertTrue(self.Organisation.IsSupplier())         
        
    def test_organisation_address_allocation(self):
        a = Address('Seaburn Road', 'Nottingham')
        a.HouseNumber = '155'
        a.LocalityName = 'Toton'
        a.PostCode = 'NG9 6HF'
        c = Country('United Kingdom')
        a.Country = c
        self.Organisation.Address = a
        
        self.assertEqual(self.Organisation.Address.AddressLine1(),'155, Seaburn Road')
        self.assertEqual(self.Organisation.Address.AddressLine2(), 'Toton')
        self.assertEqual(self.Organisation.Address.Town, 'Nottingham')
        self.assertEqual(self.Organisation.Address.PostCode, 'NG9 6HF')
        self.assertEqual(self.Organisation.Address.Country.Name, 'United Kingdom')
        
    def test_serialise(self):
        exp = '{"ClientFlag": false, "SupplierFlag": false, "Name": "Thorneycreek Consulting Ltd"}'
        s = self.Organisation.to_JSON()
        self.assertEqual(s,exp)
        
    def test_deserialise(self):
        s = self.Organisation.to_JSON()
        o = Organisation()   
        o.LoadFromJSON(s)
        self.assertEqual(o.Name, self.Organisation.Name)         