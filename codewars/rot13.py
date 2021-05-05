#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 22:42:58 2021

@author: aniket
"""

def rot13(text) : 
	"""
	text : str, input text to be ciphered, may contain punctuation or special characters which need to preserved
	returns : str, ciphered text of input text
	Eg. : "test" -> "grfg", "Test" -> "Grfg"
	"""
	cipherText = ""
	rotVal = 13
	for char in text : 
		#for each character in string get ASCII value
		chrInt = ord(char)
		subtract = 0
		#if ASCII value between 97 and 122 subtract 97
		#else between 65 and 90 so subtract 65
		if chrInt >= 97 : 
			subtract = 97
		else :
			subtract = 65
		chrInt -= subtract
		#check if within 0 and 25. 
		#If yes, add 13, then take mod wrt 26.
		if chrInt >= 0 and chrInt <= 25 : 
			chrInt += rotVal
			chrInt %= 26
		#add value subtracted in penultimate step
		chrInt += subtract
		cipherText += chr(chrInt)
	return cipherText