# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    def is_odd(num):
        return num % 2 != 0
    return filter(is_odd, number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    def is_even(num):
        return num % 2 == 0
    return filter(is_even, number_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    def check_length(word):
        return len(word) >= 4
    return filter(check_length, word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    def is_smaller(num1, num2):
        if num1 < num2:
            return num1
        else:
            return num2
    return reduce(is_smaller, number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    def is_larger(num1, num2):
        if num1 > num2:
            return num1
        else:
            return num2
    return reduce(is_larger, number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    def divide_by_2(number):
        return float(number)/2

    halved_list = map(divide_by_2, number_list)
    return halved_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    def measure_length(word):
        length = len(word)
        return length

    return map(measure_length, word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    return reduce(sums, number_list)

# Created this function for sum_numbers, need it for average as well
def sums(num1, num2):
    return num1 + num2

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    def multiply(num1, num2):
        return num1 * num2
    return reduce(multiply, number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    def combine_words(word1, word2):
        return (word1 + " " + word2)
    return reduce(combine_words, word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return (reduce(sums, number_list))/len(number_list)
