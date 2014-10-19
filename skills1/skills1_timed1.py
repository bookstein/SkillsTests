# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]
another_number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7, 1000]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    return filter(lambda num: num%2 != 0, number_list)

answer = all_odd(number_list)
print "All odds", answer

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    return filter(lambda num: num%2 == 0, number_list)

answer = all_even(number_list)
print "All evens", answer

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    return filter(lambda x: len(x)>4, word_list)

answer = long_words(word_list)
print "Long words", answer

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    def smaller(num1, num2):
        if num1 < num2:
            return num1
        else:
            return num2
    return reduce(smaller, number_list)


answer = smallest(another_number_list)
print "Smallest num", answer
# GETTING THE WRONG ANSWER --> FIXED by comparing all numbers to smallest. If a smaller num found, assign to smallest.

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    def larger(num1, num2):
        if num1 > num2:
            return num1
        else:
            return num2
    return reduce(larger, number_list)

answer = largest(another_number_list)
print "Largest num", answer
# GOT 42, NOT 1000. Didn't check last position. --> added else statement to fix

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    return map(lambda x: x/2.0, number_list)

answer = halvesies(number_list)
print "Halved nums", answer

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return map(lambda x: len(x), word_list)

answer = word_lengths(word_list)
print "Word lengths", answer

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):

    return reduce(lambda x,y: x+y, number_list)

answer = sum_numbers(number_list)
print "Sums", answer

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    return reduce(lambda x,y: x*y, number_list)

answer = mult_numbers(number_list)
print "Mult", answer

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    return reduce(lambda x, y: x + y, word_list)

answer = join_strings(word_list)
print "Joined", answer

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return reduce(lambda x,y: (x+y)/2, number_list)

answer = average(number_list)
print "Avg", answer



