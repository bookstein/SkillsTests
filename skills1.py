# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    odds = []
    for num in number_list:
        if num % 2 != 0:
            odds.append(num)
    return odds

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    evens = []
    for num in number_list:
        if num%2 == 0:
            evens.append(num)
    return evens

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    longwords = []
    for word in word_list:
        if len(word) >= 4:
            longwords.append(word)
    return longwords

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    start = number_list[0]
    for num in number_list:
        if num <= start:
            start = num
    return start

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    start = number_list[0]
    for num in number_list:
        if num >= start:
            start = num
    return start

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    halved_list = number_list[:] #this is a wasted move. how could i do it better?
    for idx in range(len(number_list)):
        halved_list[idx] = float(number_list[idx])/2
    return halved_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    lengths_list = word_list[:]
    for idx in range(len(word_list)): #when to use word in wordlist, and when to use index in len(wordlist)??
        lengths_list[idx] = len(word_list[idx])
    return lengths_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    return 0

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    return 0

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    return ""

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return 0