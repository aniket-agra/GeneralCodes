#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:24:20 2021
https://www.codewars.com/kata/54eb33e5bc1a25440d000891
NOT COMPLETE
@author: aniket
"""

def decompose(n) : 
	"""
	n : int, number to decompose
	returns : list, strictly increasing sequece of numbers 
		into which n is decomposed s.t. n^2 = sum of squares 
		of all in returned sequence. The sequence should have
		the largest numbers possible.
	Eg. : 11 -> 1, 2, 4, 10 since 11^2 = 1^2 + 2^2 + 4^2 + 10^2
	"""

	# start with subtracting (n-1)**2 from n**2. 
	# check sqrt of difference and take floor of it
	# subtract square of the floored number and get difference
	# repeat until difference = 0 
	# check if we have repeats
	# if yes start from top with subtracting (n-2)**2
	# if not reverse list and return

	out = []
	for i in range(n-1, 0, -1) : 
		out = []
		diff = n**2
		curr = i
		while diff > 0 and curr <= i : 
			out.append(curr)
			diff -= curr**2
			curr = int(diff**0.5)
		if curr <= i : 	
			outdic = {}
			dupflag = False
			for elem in out : 
				try : 
					outdic[elem] += 1
					dupflag = True
					break
				except : 
					outdic[elem] = 1
			if not dupflag : 
				break
	out.sort()
	return out