#!/usr/bin/env python3
#-*-coding:utf-8-*-
import unittest
class FirstCase01(unittest.TestCase):
    def setUp(self):
        print("这个是case的前置条件")
    def tearDown(self):
        print("这是case的后置条件")
    def testfirst01(self):
        print("这是第一条case")
    def testfirst02(self):
        print("这是第二条case")
if __name__ == '__main__':
    unittest.main()
