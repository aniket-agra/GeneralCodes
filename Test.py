#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:41:38 2021

@author: aniket
"""

class Test(object) : 
	a = 1
	def __init__(self) : 
		print("Object created.")
		self.test2Obj = Test2()
		
class Test2(Test) : 
	def __init__(self) : 
		print("Creating object of Test2 type...")
	
	def geta(self) : 
		print("Trying to access superclass variable. a = " + str(self.a))
