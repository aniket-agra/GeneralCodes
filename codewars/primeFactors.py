#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 11:07:24 2021

@author: aniket
"""

def prime_factorise(n) : 
	"""
	n : int, number to prime factorise
	returns : str, (p1**n1)(p2**n2)... where pi is an ni repeated prime factor, and p1 < p2 < p3...
	Eg : 86240 -> (2**5)(5)(7**2)(11)
	"""
	factors = ""
	if n < 0 : 
		print("Cannot factorise negative number.")
	else : 
		primeDic = {2 : 0}
		for i in range(3, int(n**0.5) + 1) : 
			prime = True
			for key in primeDic.keys() : 
				if i % key == 0 : 
					prime = False
					break
			if prime : 
				primeDic[i] = 0
		# for each prime if remainder = 0 add 1 to dict key
		# and n = n//p else move to next key
		# terminate when n <= 1 (to cover case for n = 0)
		for key in primeDic.keys() : 
			if n <= 1 : 
				break
			else : 
				while n % key == 0: 
					primeDic[key] += 1
					n = n // key
		for key in primeDic.keys() : 
			if primeDic[key] > 1 : 
				factors += "(" + str(key) + "**" + str(primeDic[key]) + ")"
			elif primeDic[key] == 1 : 
				factors += "(" + str(key) +  ")"
		# after dividing out by all primes upto sqrt(n)
		# n must be prime
		if n != 1 : 
			factors += "(" + str(n) +  ")"
	return factors