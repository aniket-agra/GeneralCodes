#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:28:35 2021
https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python
@author: aniket
"""

def title_case(title, minor_words = "") :
	"""
	title : str, text to be converted to title case
	minor_words : str, str of space-separated words to be kept in lowercase always unless they're the first word
	returns : str, in title case
	Eg : "the wind in the willows", "the IN" -> "The Wind in the Willows"
	"""
	
	# for each input we need to pre-process to ensure 
	# that cases are ignored so convert both to lowercase
	minorDic = {}
	# create a dictionary with minor_words
	minorList = minor_words.lower().split()
	for word in minorList :
		minorDic[word] = 1
	out = []
	titleList = title.lower().split()
	if len(titleList) > 0 :
		out.append(titleList[0][0].upper()+titleList[0][1:])
	for word in titleList[1:] : 
		# if in dictionary just add as is
		try : 
			if minorDic[word] == 1 : 
				out.append(word)
		# if not capitalize each word and append to a list
		except : 
			out.append(word[0].upper() + word[1:])
	# join words in list
	return " ".join(out)