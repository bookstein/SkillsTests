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
    word_list = string1.lower().split()
    for word in word_list:
    	if d.get(word):
    		d[word]+=1
    	else:
    		d.setdefault(word, 1)
    return d

# count_unique(string1)

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
    d = {}
    results = []
    # key in dict --> returns True if key is present, but I'm not allowed this
    for item in list1:
    	d[item] = 1
    for item in list2:
    	if d.get(item):
    		results.append(item)

    print results

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
    	d[item] = 1
    for item in list2:
    	if d.get(item):
    		results.append(item)

	print results

# common_items2(list1, list2)

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    results = []
    #make tuples that sum to zero
    for idx in range(len(list1)):
    	for idx_2 in range(len(list1)):
    		if list1[idx] + list1[idx_2] == 0:
    			results.append((list1[idx], list1[idx_2]))
    print results

sum_zero(list1)

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    pass

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    pass

"""
Here's a table of English to Pirate translations
English     Pirate

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

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""