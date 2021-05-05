#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 22:44:26 2021
https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python
@author: aniket
"""

def longest_consec(strarr, k) : 
	"""
	strarr : list, list of strings from which consecutive strings need to be concatenated
	k : int, no. of consecutive strings to concatenate
	returns : str, first longest string obtained by concatenating 
	Eg. : ["anike", "tree", "found"], 2 -> "aniketree" (although treefound has same length it appears later)
	"""
	n = len(strarr)
	# if k <= 0 or k > n or n == 0 where n = len(strarr) return "" 
	if k <= 0 or k > n or n == 0 : 
		return "" 
	else : 
		lenarr = []
		# generate a list of lengths of strings
		for str in strarr :
			lenarr.append(len(str))
		# initialize output string
		outstr = "" 
		maxlen = 0
		currsum = 0
		for i in range(n-k+1) : 
			# go through list of lengths adding together k @ a time
			if i == 0 :
				currsum = sum(lenarr[i:i+k])
			else : 
				currsum = currsum - lenarr[i-1] + lenarr[i+k-1]
			# if the sum is greater than last stored sum 
			# update last stored sum and corresponding outstr
			if currsum > maxlen : 
				maxlen = currsum
				outstr = ""
				for j in range(i, i+k) : 
					outstr += strarr[j]
		return outstr