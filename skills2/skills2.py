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
	pass

# count_unique(string1)

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""

# This took a long time to figure out the logic. Get a code review??
def common_items(list1, list2):
	d = {}
	results = []

	for item1 in list1:
		# all items from list1 have value 1
		d[item1] = 1
	for item2 in list2:
	# 	# if item2 is already in d, will return 1 and add 1. If not, 0 + 1.
		d[item2] = d.get(item2, 0) + 1

	print d

	for key in d.keys():
		if d[key] >= 2:

			results.append(key)

	print results
	pass

# common_items(list1, list2)



"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
	d = {}

	results = []

	for item in list1:
		d[item] = d.setdefault(item, 1)
	for item in list2:
		d[item] = d.get(item, 0) + 1

	for key in d.keys():
		if d[key] >= 2:
			results.append(key)

	print results

# common_items2(list1, list2)

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
	d = {}
	results = []

	for num in list1:
		if (-num) in list1:
			d[num] = (-num)

	for key in d.keys():
		results.append((key, d[key]))

	print results
	pass

# sum_zero(list1)

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
	d = {}
	results = []

	for word in words:
		d[word] = d.get(word, 0) + 1

	for key in d.keys():
		if d[key] > 1:
			results.append(key)

	print results
	pass

# find_duplicates(words)


"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""

#couldn't remember how to use sorted() with correct key/lambda
def word_length(words):
	d = {}

	for word in words:
		d[word] = d.get(word, len(word))

	# print d.items()

	for key, value in sorted(d.items(), key = lambda wordpair: wordpair[1]):
		print key
	pass

word_length(words)

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
	pass


