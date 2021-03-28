#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 10:36:23 2021

@author: aniket
"""

class Set(object) : 
	"""
	Set class as test class
	"""
	def ___init__(self) : 
		self.elements = []
		self.size = 0
	
	def __str__(self) : 
		if self.size > 100 : 
			print("Too many elements in set!")
		else : 
			print("{", end = "")
			for i in range(self.size) : 
				if i  !=  (self.size - 1) :
					print(self.elements[i] + ",", end = "")
				else :
					print(self.elements[i], end = "")
			print("}")
	
	def insert(self, element) : 
		self.elements.append(element)
		self.size += 1
		
	def remove(self, element) : 
		try : 
			self.elements.remove(element)
			self.size -= 1
		except ValueError : 
			print("Sorry, this element is not present in the set.")
			
	def union(self, other) : 
		newSet = Set()
		