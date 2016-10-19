from random import randint

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

