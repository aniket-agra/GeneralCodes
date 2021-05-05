#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:52:04 2021
https://www.codewars.com/kata/554a44516729e4d80b000012/train/python
@author: aniket
"""

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth) :
	""" 
	
	"""
	months = 0
	percentLossByMonth /= 100
	priceDiff = startPriceOld - startPriceNew
	balance = priceDiff
	while balance < 0 : 
		months += 1
		if months % 2 == 0 : 
			percentLossByMonth += 0.005
		priceDiff *= (1.0 - percentLossByMonth)
		balance = priceDiff + savingperMonth*months
	return [months, round(balance)]