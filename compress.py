#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

def compress(word):
	if(word == "hello"):
		return 0x3428
	else:
		return 0x3429

plain = open("plain.txt", "r")
words = plain.read().split(' ')
# print "Plain Text:"
# print words


encrypt_text = codecs.open("encrypt.txt", "w", "utf-8")
for word in words:
	# print compress(word)
	encrypt_text.write(unichr(compress(word)))
	encrypt_text.write('')

plain.close()
encrypt_text.close()

# print "Encrypted Text:"
# print open("encrypt.txt").read().split(' ')





