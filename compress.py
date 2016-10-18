#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

def encode(word):
	dic = open("dictionary", "r")
	for line in dic:
		Line = line.split(" ")
		#print Line[0]
		if (unicode(word, "utf-8") == unicode(Line[0], "utf-8")):
			return Line[1]

	return word
	

plain = open("plain.txt", "r")
words = plain.read().split(' ')
# print "Plain Text:"
# print words


encrypt_text = codecs.open("encrypt.txt", "w", "utf-8")
for word in words:
	# print compress(word)
	# encrypt_text.write(unichr(encode(word)))
	# encrypt_text.write('')
	encrypt_text.write(encode(word))

plain.close()
encrypt_text.close()

# print "Encrypted Text:"
# print open("encrypt.txt").read().split(' ')





