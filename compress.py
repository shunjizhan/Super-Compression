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
	

plain = open("plain.txt", "r")
words = plain.read().split(' ')
# print "Plain Text:"
# print words


encrypt_text = codecs.open("encrypt.txt", "w")
for word in words:
	# print compress(word)
	# encrypt_text.write(unichr(encode(word)))
	# encrypt_text.write('')
	word = encode(word)
	#print word
	encrypt_text.write(word)

plain.close()
encrypt_text.close()

# print "Encrypted Text:"
# print open("encrypt.txt").read().split(' ')





