from random import randint

plain = open("dictionary_encode", "r")
words = plain.read().split('\n')
random_file = open("random", "w")

for i in range(10000):
	randNum = randint(0, 9577)
	random_file.write(words[randNum])
	random_file.write(' ')

