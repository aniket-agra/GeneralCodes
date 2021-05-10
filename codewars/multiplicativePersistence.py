#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 22:22:19 2021
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
@author: aniket
"""

def persistence(n) : 
	"""
	n : int, number whose multiplicative persistence is to be calculated
	returns : int, persistence := number of times the digits have to be 
			multiplied with each other to get to a single digit number
	Eg. : 99 -> 2, 9x9 = 81, 8x1 = 8
	"""
	# dictionary of seen numbers
	seen = {}
	ndigits = len(str(n))
	persist = 0
	# while single digit is not reached
	while ndigits > 1 : 
		prod = 1
		# get product of digits
		for char in str(n) : 
			prod *= int(char)
		n = prod
		# if we reach a number we've already seen, we're in 
		# an infinite loop. Exit!
		if seen.get(n) : 
			return None
		# otherwise add to number of times already multiplied
		else : 
			persist += 1
		ndigits = len(str(n))
	return persist