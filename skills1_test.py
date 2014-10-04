from skills1 import *
import unittest

# word_functions = {
# 	"long_words": long_words,
# 	"word_len": word_lengths,
# 	"join_str": join_strings,
# }

# num_functions = {
# 	"odd": all_odd,
# 	"even": all_even,
# 	"sm": smallest,
# 	"larg": largest,
# 	"halve": halvesies,
# 	"sum_num": sum_numbers,
# 	"mult_num": mult_numbers,
# 	"avg": average,
# }

# print "Original number list: ", number_list
# print "Original word list: ", word_list


#print out answers
# for key in num_functions:
# 	test_num = num_functions[key](number_list)
# 	print key, test_num

# for key in word_functions:
# 	test_word = word_functions[key](word_list)
# 	print key, test_word


#why is this setup required with class? --> because it's imported from unittest library
class Test_Skills1(unittest.TestCase):

	def setUp(self):
		self.number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
		self.word_list = ["What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

#Test for all_odd
	def test_all_odd(self):
		self.assertEqual(all_odd(number_list), [-5, 15, 23, 7])

# #Test for all_even
	def test_evens(self):
		self.assertEqual(all_even(number_list), [6, 4, 8, 16, 42, 2])

# #Test for long_words
	def test_long_words(self):
		self.assertEqual(long_words(word_list), ["What", "about", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "spam"])

# #Test for smallest
	def test_smallest(self):
		self.assertEqual(smallest(number_list), -5)

# #Test for largest
	def test_largest(self):
		self.assertEqual(largest(number_list), 42)

# #Test for halvesies
	def test_halvesies(self):
		self.assertEqual(halvesies(number_list), [-2.5, 3.0, 2.0, 4.0, 7.5, 8.0, 11.5, 21.0, 1.0, 3.5])

#Test for word_lengths
	def test_word_lengths(self):
		self.assertEqual(word_lengths(word_list), [4, 5, 3, 4, 7, 4, 4, 5, 4, 6, 3, 4])

#Test for sum_numbers
	def test_sum(self):
		self.assertEqual(sum_numbers(number_list), 118)

	def test_mult_nums(self):
		self.assertEqual(mult_numbers(self.number_list), -3115929600)

	def test_join_str(self):
		self.assertEqual(join_strings(self.word_list), "What about the Spam sausage spam spam bacon spam tomato and spam")

	def test_average(self):
		self.assertEqual(average(self.number_list), 11)


if __name__ == '__main__':
	 unittest.main()

