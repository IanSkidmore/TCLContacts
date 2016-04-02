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