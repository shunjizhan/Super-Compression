
random = open("random", "r")
random_modified = open("random_modified", "w")
words = random.read().split(' ')

#print words
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


