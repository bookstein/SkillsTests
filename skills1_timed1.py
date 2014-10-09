# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    return filter(lambda num: num%2 != 0, number_list)

answer = all_odd(number_list)
print answer

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    return filter(lambda num: num%2==0, number_list)

answer = all_even(number_list)
print answer

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    return filter(lambda word: len(word) >= 4, word_list)

answer = long_words(word_list)
print answer

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    def smaller(num1, num2):
        if num1 < num2:
            return num1
        else:
            return num2
    return reduce(smaller, number_list)

answer = smallest(number_list)
print answer

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    def larger(num1, num2):
        if num1 < num2:
            return num2
        else:
            return num1
    return reduce(larger, number_list)

answer = largest(number_list)
print answer

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    return map(lambda x: x/2.0, number_list)

answer = halvesies(number_list)
print answer

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return map(lambda word: len(word), word_list)

answer = word_lengths(word_list)
print answer

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    def sum_num(num1, num2):
        return num1 + num2
    return reduce(sum_num, number_list)

answer = sum_numbers(number_list)
print answer

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    return reduce(lambda x,y: x*y, number_list)

answer = mult_numbers(number_list)
print answer

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    def join(word1, word2):
        return word1 + word2
    return reduce(join, word_list)

answer = join_strings(word_list)
print answer

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    def avg(num1, num2):
        return (num1 + num2)/2
    return reduce(avg, number_list)

answer = average(number_list)
print answer