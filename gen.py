#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

def compress(word):
	if(word == "hello"):
		return 0x3428
	else:
		return 0x3429

plain = open("dictionary_encode", "r")
words = plain.read().split('\n')
# print "Plain Text:"
# print words


dic = codecs.open("dictionary", "w", "utf-8")
character = 0x3428
for word in words:
	# print compress(word)
	if (len(word) > 2):
		dic.write(word)
		dic.write(' ')
		dic.write(unichr(character))
		dic.write('\n')
		character += 1

plain.close()
dic.close()