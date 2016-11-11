# IMPORTS #
from random import *
from sys import *
from collections import defaultdict


#dummy var
var = 0;


class Markov_Chain:
	global markov_chain 
	markov_chain = defaultdict(list)


	def create_markov(input):


		# open and parse the text file
		open_input = open('test.txt', 'r')
		# pass it to a string
		input_string = open_input.read()
		#split into an array
		words = input_string.split()
		#print the split array for debugging
		# print(words)

		#store a list of subsequents in each dictionary word entry
		for i, word in enumerate(words):
				# try append next to dictionary if a next word exists
			try:
				markov_chain[word].append(words[i+1])
			except:
				print "gay"
		print(markov_chain)

	def create_output(length):
		#if input length is zero, create a random length
		if length == 0:
			length = randint(1, 50)

		outputString = "OUTPUT STRING: "
		outputString += str(choice(list(markov_chain)))

		for word in range(length):

			parseOutput = outputString.split()
			#random access number which is length of possible options for each word
			answerLength = len(markov_chain[parseOutput[-1]])
			#access last element in list and find in dictionary
			try:
				outputString += ' '.join(markov_chain[parseOutput[-1]])
				print answerLength
			except:
				print "length out of range exception"
				print answerLength


		print (outputString)




newchain = Markov_Chain()
newchain.create_markov()
newchain.create_output()




