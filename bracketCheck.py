#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 22:21:35 2021

@author: aniket
"""

def bracketCheck(s) : 
	"""
	Check if the opening and closing brackets match up in s.
	s : str
	return : boolean, True if brackets match up, False otherwise
	"""
	correspond = {'}' : '{', ']' : '[', ')' : '('}
	brackets = []
	for char in s : 
		if char == '{' or char == '(' or char == '[' : 
			brackets.append(char)
		elif char == '}' or char == ')' or char == ']' : 
			try : 
				if brackets[-1] == correspond[char] : 
					brackets = brackets[:-1]
				else :
					return False
			except : 
				return False
	if len(brackets) == 0 : 
		return True
	else :
		return False