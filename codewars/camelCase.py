# -*- coding: utf-8 -*-

def camelCase(text) : 
	"""
	text : str, text to be converted to camel case
	returns : str, camel case of entered text
	Eg. : "the_Serpent-isDead" -> "theSerpentIsDead"
	"""
	words = []
	curr = ""
	#run through the string to extract words to a list
	for char in text : 
		#if a - or _ is encountered append the so-far stored characters to the list and flush. Repeat.
		if char == "-" or char == "_" : 
			if len(curr) > 0 : 
				words.append(curr)
				curr = ""
		#keep storing characters until a - or _ is encountered
		else : 
			curr += char
	if curr != "" :
		words.append(curr)
	camelWords = []
	if len(words) > 0 : 
		camelWords.append(words[0])
		#go through list and capitalize first letter of each word starting from 2nd word
		for word in words[1:] :
			camelWord = word[0].upper()+word[1:]
			camelWords.append(camelWord)
	#join words in list
	return "".join(camelWords)