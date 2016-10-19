#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from cStringIO import StringIO
import codecs
import os
from trie import Trie

############# encode() #############
def encode(word): ## TODO convert Upper to lower
	dic = open("dictionary", "r")
	if (word == '\n'):
		return "00000000000000"
	else:
		for line in dic:
			Line = line.split(" ")

			if (word == Line[0]):
				return Line[1].strip('\n')

	return "11111111111111"   # unrecognized word

############# decode() #############
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

############# modify_bi(bi) #############
def modify_bi(bi):
	plus = 14-len(bi)
	for i in range(0, plus):
		bi = '0' + bi
	return bi

############# rand_gen() #############
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

############# modify() #############
def modify(file):
	random = open(file, "r")
	modified_file = open("modified_file", "w")
	words = random.read().split(' ')

	#c = []
	#cc = []
	for word in words:
		#cc.append(word)
		if ('\n' in word):
			position = word.find('\n')
			modified_file.write(word[0:position-1])  
		#	c.append(word[0:position-1])
			modified_file.write(' ')
			modified_file.write(word[position-1])  
		#	c.append(word[position-1])
			modified_file.write(' ')
			modified_file.write(word[position])
		#	c.append(word[position])
			modified_file.write(' ')
			if ((word[-1:] == ',') or (word[-1:] == '.')):
				modified_file.write(word[position+1:-1])
			#	c.append(word[position+1:-1])
				modified_file.write(' ')
				modified_file.write(word[-1:])
			#	c.append(word[-1:])
				modified_file.write(' ')
			else:
				modified_file.write(word[position+1:])
			#	c.append(word[position+1:])
				modified_file.write(' ')

		elif ((word[-1:] == ',') or (word[-1:] == '.')):
			word_split = word.split()
			modified_file.write(word[0:-1])
		#	c.append(word[0:-1])
			modified_file.write(' ')
			modified_file.write(word[-1:])
		#	c.append(word[-1:])
			modified_file.write(' ')

		else:
			modified_file.write(word)
		#	c.append(word)
			modified_file.write(' ')

	#print cc
	#print c
	random.close()
	modified_file.close()
	print "finished modifying!"


############# set_up_dict() #############
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

############# compress() #############
def compress():
	rand = open("modified_file", "r")	# open the random generated file
	rand_words = rand.read().split(' ')

	sum = 0
	num = 0
	string = ''
	for rand_word in rand_words:		# encode each word
		if not(rand_word == ''):
			sum += len(rand_word)
			num += 1
			string += trie.search(rand_word)

	# now string contains binary encoding of the whole text
	sio = StringIO(string)
	f = open('super_compressed_file', 'wb')

	while 1:
	    b = sio.read(8)

	    if not b:
	        break
	    print b
	    i = int(b, 2)
	    c = chr(i)

	    f.write(c)

	rand.close()
	f.close()

	print "Finished encoding!!!"
	avg = sum*1.0/num
	ratio = 14/(avg*8)
	print "average word length: %.2f" % avg
	print "expected compression ratio: %.3f" % ratio

############# decompress() #############
def decompress():
	# first read all the binary data from file
	f = open("super_compressed_file", "rb")
	word = f.read()

	string = ''
	for char in word:
		# string += str(ord(char))
		word = "{0:b}".format(ord(char))
		word = '0'*(8-len(word)) + word
		#print word
		#write.write(word)
		string += word

	f.close()

	# decode binary data to plain text
	write = open("decoded_file", "w")
	file = string

	i = 0
	word = ""
	words = []
	while (i <len(file)):
		word += file[i]
		i += 1
		if (i%14 == 0):
			words.append(trie1.search(word))
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

########## trie_setup() ##########
def trie_setup(s):
	dic = open(s,"r")
	for line in dic:
		Line = line.split(" ")
		trie.add(Line[0],Line[1].strip("\n"))
		trie1.add(Line[1].strip("\n"),Line[0])




############# run() #############
def run(plain_file):


	rand_gen(1000)	# generate a random text file
	modify(plain_file)	# modify the text file
	set_up_dict()	# set up the bijection dictionary
	trie.add('\n','00000000000000')
	trie1.add('00000000000000','\n')
	trie_setup("dictionary")
	compress()	# encode the text file 
	decompress()

	before = os.stat(plain_file).st_size
	after = os.stat('super_compressed_file').st_size
	print "finished compressing %s(%dKB) to super_compressed_file(%dKB)!" % (plain_file, before, after)
	print "compression ratio: %.3f" % (after*1.0/before)


############# main() #############
file = "random_generated_file"
trie=Trie()
trie1=Trie()
run(file)







