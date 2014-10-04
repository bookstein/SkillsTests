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
    def divide_by_2(number):
        return float(number)/2

    halved_list = map(divide_by_2, number_list)
    return halved_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    # #lengths_list = word_list[:]
    # lengths_list = []
    # for word in word_list: #when to use word in wordlist, and when to use index in len(wordlist)??
    #     lengths_list.append(len(word))
    # return lengths_list
    def measure_length(word):
        length = len(word)
        return length

    lengths_list = map(measure_length, word_list)
    return lengths_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    total = 0
    for num in number_list:
        total += num
    return total

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    total = number_list[0]
    for num in number_list[1:]:
        total = total * num
    return total

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    new_string = ""
    for word in word_list:
        new_string = new_string + " " + word
    return new_string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    total = 0
    for num in number_list:
        total = total + num
    average = total/len(number_list)
    return average