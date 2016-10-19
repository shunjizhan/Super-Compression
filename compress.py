#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
import codecs

def modify_bi(bi):
	plus = 14-len(bi)
	for i in range(0, plus):
		bi = '0' + bi
	return bi

########## rand_gen() ##########
def rand_gen(num):
	plain = open("dictionary_encode", "r")
	words = plain.read().split('\n')
	random_file = open("random", "w")

	for i in range(num):
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
	if (word == '\n'):
		return "00000000000000"
	else:
		for line in dic:
			Line = line.split(" ")

			if (word == Line[0]):
				return Line[1].strip('\n')

	return "11111111111111"   # unrevognized word

########## modify() ##########
def modify(file):
	random = open(file, "r")
	random_modified = open("random_modified", "w")
	words = random.read().split(' ')

	#c = []
	cc = []
	for word in words:
		cc.append(word)
		if ('\n' in word):
			position = word.find('\n')
			random_modified.write(word[0:position-1])  
		#	c.append(word[0:position-1])
			random_modified.write(' ')
			random_modified.write(word[position-1])  
		#	c.append(word[position-1])
			random_modified.write(' ')
			random_modified.write(word[position])
		#	c.append(word[position])
			random_modified.write(' ')
			if ((word[-1:] == ',') or (word[-1:] == '.')):
				random_modified.write(word[position+1:-1])
			#	c.append(word[position+1:-1])
				random_modified.write(' ')
				random_modified.write(word[-1:])
			#	c.append(word[-1:])
				random_modified.write(' ')
			else:
				random_modified.write(word[position+1:])
			#	c.append(word[position+1:])
				random_modified.write(' ')

		elif ((word[-1:] == ',') or (word[-1:] == '.')):
			word_split = word.split()
			random_modified.write(word[0:-1])
		#	c.append(word[0:-1])
			random_modified.write(' ')
			random_modified.write(word[-1:])
		#	c.append(word[-1:])
			random_modified.write(' ')

		else:
			random_modified.write(word)
		#	c.append(word)
			random_modified.write(' ')

	print cc
	#print c
	random.close()
	random_modified.close()
	print "finished modifying!"


########## set_up_dict() ##########
def set_up_dict():
	plain = open("dictionary_encode", "r")  # open the English dictionary
	words = plain.read().split('\n')

	dic = codecs.open("dictionary", "w", "utf-8") # open the bijection dictionary
	#character = 0x0080  
	num = 1  

	for word in words:		# set up bijection for each word
		#if ((len(word) > 2) or (word == ',') or (word == '.') or (word == '\n')):	
			dic.write(word)
			dic.write(' ')
			#dic.write(unichr(character))
			binary = str('{0:1b}'.format(num))
			dic.write(modify_bi(binary))
			dic.write('\n')
			#character += 1
			num += 1

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
	print word
	if (word == '00000000000000'):
		return '\n'
	else:
		dic = open("dictionary", "r")
		for line in dic:
			Line = line.split(" ")

			if (word == Line[1].strip('\n')):
				return Line[0]

	return '###unrecognized_word####'

########## decompress() ##########
def decompress():
	en = codecs.open("encrypt", "r", "utf-8")
	string = en.read()		
	decrypt_text = codecs.open("decrypt", "w")

	i = 0
	word = ''

	input = []
	while(i < len(string)):
		word += string[i]
		i += 1
		if (i%14 == 0):
			#decrypt_text.write(decode(word))
			input.append(decode(word))
			word = ''
	k = 0
	while(k < len(input)):
		if ((k+1 < len(input)) and ((input[k+1] == ',') or (input[k+1] == '.'))):
			decrypt_text.write(input[k])
			decrypt_text.write(input[k+1])
			decrypt_text.write(' ')
			k += 2
		elif (input[k] == '\n'):
			decrypt_text.write(input[k])
			k += 1
		else:
			decrypt_text.write(input[k])
			decrypt_text.write(' ')
			k += 1

	en.close()
	decrypt_text.close()

	print "Finished decoding!!!"

def modify_hex(word):
	if (len(word) == 2):
		return word
	else:
		return '0' + word	

def encode_hex():
	file = open("encrypt", "r")
	string = file.read()
	plus = 16 - (len(string) % 16)
	for k in range(0, plus):
		string += '0'
	encode = open("encode_hex", "w")

	i = 0
	word = ''

	while(i < len(string)):
		word += string[i]
		i += 1
		if (i%8 == 0):
			word = modify_hex(hex(int(word, 2)).strip('0x'))
			if (len(word) == 2):
				encode.write(word)
				encode.write(' ')
				word = ''
	

########## run() ##########
def run(plain_file):
	rand_gen(10)	# generate a random text file
	modify(plain_file)	# modify the text file
	set_up_dict()	# set up the bijection dictionary
	compress()	# encode the text file
	encode_hex()
	decompress()


########## main() ##########
file = "random"
run(file)






