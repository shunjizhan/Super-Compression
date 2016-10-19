#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from cStringIO import StringIO
import codecs
import os


def modify_bi(bi):
	plus = 14-len(bi)
	for i in range(0, plus):
		bi = '0' + bi
	return bi

########## rand_gen() ##########
def rand_gen(num):
	plain = open("dictionary_encode", "r")
	words = plain.read().split('\n')
	random_file = open("random_generated_file", "w")

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

	return "11111111111111"   # unrecognized word

########## modify() ##########
def modify(file):
	random = open(file, "r")
	random_modified = open("random_modified", "w")
	words = random.read().split(' ')

	#c = []
	#cc = []
	for word in words:
		#cc.append(word)
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

	#print cc
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
		if not(rand_word == ''):
			sum += len(rand_word)
			num += 1
			encrypt_text.write(encode(rand_word))

	rand.close()
	encrypt_text.close()

	print "Finished encoding!!!"
	avg = sum*1.0/num
	ratio = 14/(avg*8)
	print "average word length: %.2f" % avg
	print "expected compression ratio: %.3f" % ratio


########## decode() ##########
def decode(word):
	#print word
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
				if (i%16 == 0):
					encode.write(' ')
				word = ''

	test(string)

def test(string):

	sio = StringIO(string)

	f = open('super_compressed_file', 'wb')

	while 1:
	    # Grab the next 8 bits
	    b = sio.read(8)
	    #print b

	    # Bail if we hit EOF
	    if not b:
	        break

	    # If we got fewer than 8 bits, pad with zeroes on the right
	    if len(b) < 8:
	        b = b + '0' * (8 - len(b))

	    # Convert to int
	    i = int(b, 2)
	    #print i

	    # Convert to char
	    c = chr(i)
	    #print c

	    # Write
	    f.write(c)

	f.close()

def de():
	# first read all the binary data from file
	f = open("super_compressed_file", "rb")
	write = open("realdecode", "w")
	word = f.read()
	#print word
	string = ''
	for char in word:
		# string += str(ord(char))
		word = "{0:b}".format(ord(char))
		word = '0'*(8-len(word)) + word
		#print word
		write.write(word)

	f.close()
	write.close()

	# decode binary data to plain text
	f = open("realdecode", "r")
	write = open("realplain", "w")
	file = f.read()

	i = 0
	word = ""
	words = []
	while (i <len(file)):
		word += file[i]
		i += 1
		if (i%14 == 0):
			words.append(decode(word))
			#write.write(decode(word))
			#write.write(' ')
			word = ""

	k = 0
	while(k < len(words)):
		if ((k+1 < len(words)) and ((words[k+1] == ',') or (words[k+1] == '.'))):
			write.write(words[k])
			write.write(words[k+1])
			write.write(' ')
			k += 2
		elif (words[k] == '\n'):
			write.write(words[k])
			k += 1
		else:
			write.write(words[k])
			write.write(' ')
			k += 1


	f.close()
	write.close()



	

########## run() ##########
def run(plain_file):
	rand_gen(1000)	# generate a random text file
	modify(plain_file)	# modify the text file
	#set_up_dict()	# set up the bijection dictionary
	compress()	# encode the text file #*****#
	encode_hex()
	#decompress()
	de()

	before = os.stat(plain_file).st_size
	after = os.stat('super_compressed_file').st_size
	print "finished compressing %s(%dKB) to super_compressed_file(%dKB)!" % (plain_file, before, after)
	print "compression ratio: %.3f" % (after*1.0/before)


########## main() ##########
file = "random_generated_file"
run(file)







