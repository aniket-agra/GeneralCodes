#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 22:35:49 2021

@author: aniket
"""

class Node(object) : 
	def __init__(self, val = None, nextNode = None) :
		self.val = val
		self.next = nextNode

	def setVal(self, val) : 
		self.val = val
		
	def setNext(self, nextNode) : 
		self.next = nextNode
	
	def getVal(self) : 
		return self.val
	
	def getNext(self) : 
		return self.nextNode

class linkedList(object) : 
	def __init__(self, head = None) : 
		self.head = head
		
	