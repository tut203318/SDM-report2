#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_sample5 (self):
                self.assertEqual (21, calc(7,3))

        def test_sample6 (self):
                self.assertEqual (-1, calc(-1,43))

        def test_sample7 (self):
                self.assertEqual (-1, calc(9,-5))
        
        def test_sample8 (self):
                self.assertEqual (-1, calc(10,1001))

        def test_sample9 (self):
                self.assertEqual (-1, calc(9,10.5))

        def test_sample10 (self):
                self.assertEqual (-1, calc(4.2,90))
        
        def test_sample11 (self):
                self.assertEqual (-1, calc("abc",1))
        
        def test_sample12 (self):
                self.assertEqual (-1, calc(1,"def"))

        def test_sample13 (self):
                self.assertEqual (-1, calc("１０",1))

        def test_sample14 (self):
                self.assertEqual (-1, calc(2,"２０"))


