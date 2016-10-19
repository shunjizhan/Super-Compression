#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
import codecs


########## rand_gen() ##########
def rand_gen():
	plain = open("dictionary_encode", "r")
	words = plain.read().split('\n')
	random_file = open("random", "w")

	for i in range(10000):
		randNum = randint(0, 9577)
		random_file.write(words[randNum])
		if (randNum < 1000):	# 10%
			random_file.write(',')
			random_file.write(' ')
		elif (randNum > 9000):	# 10%
			random_file.write('.')
			random_file.write(' ')
		elif not(randNum < 1200): 
			random_file.write(' ')
		else:					# 2%
			random_file.write(".\n")

	plain.close()
	random_file.close()
	print "finished generating text!"

########## encode() ##########
def encode(word):
	dic = open("dictionary", "r")
	for line in dic:
		Line = line.split(" ")

		if (word == Line[0]):
			return Line[1].strip('\n')

	return word

########## modify() ##########
def modify(file):
	random = open(file, "r")
	random_modified = open("random_modified", "w")
	words = random.read().split(' ')

	for word in words:
		lastchar = word[-1:]
		if ((lastchar == ',') or (lastchar == '.')):
			word_split = word.split()
			random_modified.write(word[0:-1])
			random_modified.write(' ')
			random_modified.write(word[-1:])
			random_modified.write(' ')

		elif ('\n' in word):
			position = word.find('\n')
			random_modified.write(word[0:position-1]) # .
			random_modified.write(' ')
			random_modified.write(word[position-1]) # \n
			random_modified.write(' ')
			random_modified.write(word[position])
			random_modified.write(' ')
			random_modified.write(word[position+1:])
			random_modified.write(' ')

		else:
			random_modified.write(word)
			random_modified.write(' ')

	random.close()
	random_modified.close()
	print "finished modifying!"


########## set_up_dict() ##########
def set_up_dict():
	plain = open("dictionary_encode", "r")  # open the English dictionary
	words = plain.read().split('\n')

	dic = codecs.open("dictionary", "w", "utf-8") # open the bijection dictionary
	character = 0x0080     

	for word in words:		# set up bijection for each word
		if (len(word) > 2):	
			dic.write(word)
			dic.write(' ')
			dic.write(unichr(character))
			dic.write('\n')
			character += 1

	plain.close()
	dic.close()
	print "finished setting up dictionary!"

########## compress() ##########
def compress():
	rand = open("random_modified", "r")			# open the random generated file
	rand_words = rand.read().split(' ')

	encrypt_text = codecs.open("encrypt", "w")
	sum = 0
	num = 0
	for rand_word in rand_words:		# encode each word
		sum += len(rand_word)
		num += 1
		encrypt_text.write(encode(rand_word))

	rand.close()
	encrypt_text.close()

	print "Finished encoding!!!"
	print "average word length:",
	print sum*1.0/num


########## decode() ##########
def decode(word):
	dic = open("dictionary", "r")
	print word
	for line in dic:
		Line = line.split(" ")

		if (word == Line[1]):
			print "!!!!!"
			return Line[0].strip('\n')

	return word

########## decompress() ##########
def decompress():
	en = codecs.open("encrypt", "r", "utf-8")
	line = en.readlines()			
	words = []
	for i in range(0, len(line)):
		words.append(line[i])

	decrypt_text = codecs.open("decrypt", "w")
	for word in words:		# decode each word
		decrypt_text.write(decode(word))

	en.close()
	decrypt_text.close()

	print "Finished decoding!!!"

########## run() ##########
def run(plain_file):
	rand_gen()	# generate a random text file
	modify(plain_file)	# modify the text file
	set_up_dict()	# set up the bijection dictionary
	#compress()	# encode the text file
	decompress()


########## main() ##########
file = "random"
run(file)






