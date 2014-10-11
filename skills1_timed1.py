# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]
another_number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7, 1000]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    result = []
    for num in number_list:
        if num % 2 != 0:
            result.append(num)
    return result

answer = all_odd(number_list)
print "All odds", answer

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    result= []
    for num in number_list:
        if num % 2 ==0:
            result.append(num)
    return result

answer = all_even(number_list)
print "All evens", answer

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    str_lengths = []
    for word in word_list:
        if len(word) >= 4:
            str_lengths.append(word)
    return str_lengths

answer = long_words(word_list)
print "Long words", answer

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    for index in range(1, len(number_list)):
        smallest = number_list[0]
        if number_list[index] < smallest:
            smallest = number_list[index]
            print smallest
    return smallest

answer = smallest(another_number_list)
print "Smallest num", answer
# GETTING THE WRONG ANSWER --> FIXED by comparing all numbers to smallest. If a smaller num found, assign to smallest.

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    largest = None
    for index in range(len(number_list) - 1):
        if number_list[index] > number_list[index +1]:
            largest = number_list[index]
        else:
            largest = number_list[index +1]
    return largest

answer = largest(another_number_list)
print "Largest num", answer
# GOT 42, NOT 1000. Didn't check last position. --> added else statement to fix

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    result = []
    for index in range(len(number_list)):
        result.append(number_list[index]/2.0)
    return number_list

answer = halvesies(number_list)
print "Halved nums", answer

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    result = []
    for word in word_list:
        result.append(len(word))
    return result

answer = word_lengths(word_list)
print "Word lengths", answer

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    print number_list
    total = 0
    for num in number_list:
        total += num
    return total

answer = sum_numbers(number_list)
print "Sums", answer

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    total = 1
    for num in number_list:
        total *= num
    return total

answer = mult_numbers(number_list)
print "Mult", answer

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    full_string = ""
    for word in word_list:
        full_string = full_string + "" + word
    return full_string

answer = join_strings(word_list)
print "Joined", answer

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    total = 0
    for num in number_list:
        total += num
    return total/(len(number_list))

answer = average(number_list)
print "Avg", answer