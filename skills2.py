string1 = "I do not like green eggs and ham. Do you like green eggs and ham?"
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
	d = {}

	words = string1.split()
	for word in words:
		d[word] = d.get(word, 0) + 1

	print d

# count_unique(string1)

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
	list1_items = set(list1)
	list2_items = set(list2)

	print list1_items & list2_items

# common_items(list1, list2)



"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
	d = {}
	for item in list1:
		if item in list2:
			d[item] = d.get(item, 0) + 1

	print sorted(d.keys())

# common_items2(list1, list2)

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
	d = {}

	for num in list1:
		for idx in range(len(list1)):
			if num + list1[idx] == 0:
				d[num] = list1[idx]
	print d


# sum_zero(list1)

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
	d = {}
	for word in words:
		d[word] = d.get(word, 0)

	print d.keys()

# find_duplicates(words)


"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
	d = {}

	for word in words:
		d[word] = len(word)

	for key, value in sorted(d.items(), key = lambda x: x[1], reverse = False):
		print key, value

# word_length(words)

import string

"""
Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""
pirate_translations ="""
sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey
"""

def make_dictionary(translations):
	translation_dictionary = {}

	translations = translations.strip()
	# print translations
	translations = translations.split('\n')
	# print translations


	for word_pair in translations:
		word_pair = word_pair.strip()
		# splits word pairs apart by double-spaces
		word_pair = word_pair.split("  ")
		# to get rid of empty extra spaces inside word_pair list:
		english = word_pair[0]
		pirate = word_pair[-1]
		word_pair = [english, pirate]

		print word_pair
		translation_dictionary[word_pair[0]] = word_pair[1:]

	return translation_dictionary

def translate(sentence, dictionary):
	sentence = sentence.strip()
	words = sentence.split()

	translation = []
	for word in words:
		# to remove punctuation from word for dictionary lookup:
		# however, this is inefficient and runs through each word multiple times
		for punc in string.punctuation:
			word = word.replace(punc, "")
			# print word
		word = dictionary.get(word, word)

		translation.append(word)

	print translation

	# return " ".join(translation)

pirate_dictionary = make_dictionary(pirate_translations)
translate("Get me a lawyer sir. I cannot abide this hotel.", pirate_dictionary)



