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
	def __init__(self, initial = []) : 
		self.elements = initial
		self.size = len(initial)
	
	def __str__(self) : 
		retStr = ""
		if self.size > 100 : 
			retStr = "Too many elements in set!"
		else : 
			retStr = "{"
			for i in range(self.size) : 
				retStr += str(self.elements[i])
				if i  !=  (self.size - 1) :
					 retStr += ", "
			retStr += "}"
		return retStr
	
	def insert(self, element) : 
		if element not in self.elements : 
			self.elements.append(element)
			self.size += 1
		else : 
			print("Element " + str(element) + " is already in the set.", 
				 end = " ")
			print("Set only supports unique elements.")
		
	def remove(self, element) : 
		try : 
			self.elements.remove(element)
			self.size -= 1
		except ValueError : 
			print("Element " + str(element) + " is not present in the set.")
			
	def union(self, other) : 
		unionSet = Set()
		for elem in self.elements : 
			unionSet.insert(elem)
		for elem in other.elements : 
			unionSet.insert(elem)
		return unionSet
	
	def intersection(self, other) : 
		intersectSet = Set()
		for elem in self.elements : 
			if elem in other.elements : 
				intersectSet.insert(elem)
		return intersectSet