#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

def encode(word):
	dic = open("dictionary", "r")
	for line in dic:
		Line = line.split(" ")
		#print Line[0]
		#print word
		#if (unicode(word, "utf-8") == unicode(Line[0], "utf-8")):
		if (word == Line[0]):
			return Line[1].strip('\n')

	return word

print "start to set up dictionary..."
plain = open("dictionary_encode", "r")  # open the English dictionary
words = plain.read().split('\n')

dic = codecs.open("dictionary", "w", "utf-8") # open the bijection dictionary
character = 0x0080      
sum = 0
for word in words:		# set up bijection for each word
	sum += len(word)
	if (len(word) > 2):	
		dic.write(word)
		dic.write(' ')
		dic.write(unichr(character))
		dic.write('\n')
		character += 1

print "average length of the words:",
print sum*1.0/len(words)
plain.close()
dic.close()
print "finished set up dictionary"


######### Start to encode and compress #########
print "start to encode..."
rand = open("random", "r")			# open the random generated file
rand_words = rand.read().split(' ')

encrypt_text = codecs.open("encrypt", "w")
for rand_word in rand_words:		# encode each word
	encrypt_text.write(encode(rand_word))

plain.close()
encrypt_text.close()

print "Finished!!!"




