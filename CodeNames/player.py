#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 10:57:23 2021

@author: aniket
"""

from game import Game

class Player(Game) : 
	#each player has a color and a property of being Master	
	def __init__(self, color, isMaster = False) :
		self.color = color
		self.isMaster = isMaster 
	
	#each player may print the board for a given Game instance
	def printBoard(self, gameObj) : 
		if isinstance(gameObj, Game) : 
			gameObj.printBoard()
			return 1
		else : 
			print("Sorry, can't print board for given game instance.")
			return 0
		
	#Masters may print key
	def printKey(self, gameObj) : 
		if self.isMaster : 
			gameObj.printKey()
		else : 
			print("Sorry, you cannot view the key")
			
	#get isMaster
	def getIsMaster(self) : 
		return self.isMaster 
	
	#getColor
	def getColor(self) : 
		return self.color
	