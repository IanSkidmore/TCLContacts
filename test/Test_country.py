# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 16:36:08 2016

@author: IAN
"""

import unittest

from country import Country

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.Country = Country('United Kingdom')
        
    def tearDown(self):
        self.Country = None
        
    def test_country_initialisation(self):
        self.assertEqual(self.Country.Name, 'United Kingdom')
        
    def test_serialise(self):
        exp = '{"Name": "United Kingdom"}'
        s = self.Country.to_JSON()
        self.assertEqual(s,exp)
        
    def test_deserialise(self):
        s = self.Country.to_JSON()
        c = Country()   
        c.LoadFromJSON(s)
        self.assertEqual(c.Name, self.Country.Name)          