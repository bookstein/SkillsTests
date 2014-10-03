from skills1 import *
import unittest

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

print "Original number list: ", number_list
print "Original word list: ", word_list

word_functions = {
	"long_words": long_words,
	"word_len": word_lengths,
	"join_str": join_strings,
}

num_functions = {
	"odd": all_odd,
	"even": all_even,
	"sm": smallest,
	"larg": largest,
	"halve": halvesies,
	"sum_num": sum_numbers,
	"mult_num": mult_numbers,
	"avg": average,
}

#print out answers
for key in num_functions:
	test_num = num_functions[key](number_list)
	print key, test_num

for key in word_functions:
	test_word = word_functions[key](word_list)
	print key, test_word

#verify answers match expected answers
# class TestListOperations(unittest.TestCase):

#     def setUp(self):
#         self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
#                        'Sep', 'Oct', 'Nov', 'Dec']
#         self.notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
#         self.multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

#     ### Tests for Part 1 ###

#     def test_1_A_head(self):
#         self.assertEqual(head(self.months), 'Jan')
#         self.assertEqual(head(self.notes), 'Do')
#         self.assertEqual(head(self.multiples), 0)

#

#     ### Tests for Part 2 ###

#     def test_2_A_custom_len(self):
#         self.assertEqual(custom_len(self.months), 12)
#         self.assertEqual(custom_len(self.notes), 8)
#         self.assertEqual(custom_len(self.multiples), 10)

#     def test_2_B_custom_append(self):
#         custom_append(self.months, 'Hex')
#         custom_append(self.notes, 'Re')
#         custom_append(self.multiples, 30)

#         self.assertEqual(self.months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#                                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
#                                        'Hex'])
#         self.assertEqual(self.notes, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
#                                       'Do', 'Re'])
#         self.assertEqual(self.multiples, [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

#     def test_2_C_custom_extend(self):
#         custom_extend(self.months, ['Bin', 'Tri', 'Hex'])
#         custom_extend(self.notes, ['Re', 'Mi', 'Fa', 'So'])
#         custom_extend(self.multiples, [30, 33, 36, 39, 42, 45])

#         self.assertEqual(self.months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#                                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
#                                        'Bin', 'Tri', 'Hex'])
#         self.assertEqual(self.notes, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
#                                       'Do', 'Re', 'Mi', 'Fa', 'So'])
#         self.assertEqual(self.multiples, [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30,
#                                           33, 36, 39, 42, 45])

#     def test_2_D_custom_insert(self):
#         custom_insert(self.months, 8, 'Hex')
#         custom_insert(self.notes, len(self.notes), 'Re')
#         custom_insert(self.multiples, 0, -3)

#         self.assertEqual(self.months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#                                        'Jul', 'Aug', 'Hex', 'Sep', 'Oct', 'Nov',
#                                        'Dec'])
#         self.assertEqual(self.notes, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
#                                       'Do', 'Re'])
#         self.assertEqual(self.multiples, [-3, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

#     def test_2_E_custom_remove(self):
#         custom_remove(self.months, 'Jul')
#         custom_remove(self.notes, 'Do')
#         custom_remove(self.multiples, 27)

#         self.assertEqual(self.months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#                                        'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
#         self.assertEqual(self.notes, ['Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'])
#         self.assertEqual(self.multiples, [0, 3, 6, 9, 12, 15, 18, 21, 24])

#     def test_2_F_custom_pop(self):
#         self.assertEqual(custom_pop(self.months), 'Dec')
#         self.assertEqual(custom_pop(self.notes), 'Do')
#         self.assertEqual(custom_pop(self.multiples), 27)

#         self.assertEqual(self.months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#                                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov'])
#         self.assertEqual(self.notes, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti'])
#         self.assertEqual(self.multiples, [0, 3, 6, 9, 12, 15, 18, 21, 24])

#     def test_2_G_custom_index(self):
#         self.assertEqual(custom_index(self.months, 'Jul'), 6)
#         self.assertEqual(custom_index(self.notes, 'Do'), 0)
#         self.assertEqual(custom_index(self.multiples, 27), 9)

#     def test_2_H_custom_count(self):
#         self.assertEqual(custom_count(self.months, 'Jul'), 1)
#         self.assertEqual(custom_count(self.notes, 'Do'), 2)
#         self.assertEqual(custom_count(self.multiples, 27), 1)

#     def test_2_I_custom_reverse(self):
#         custom_reverse(self.months)
#         custom_reverse(self.notes)
#         custom_reverse(self.multiples)

#         self.assertEqual(self.months, ['Dec', 'Nov', 'Oct', 'Sep', 'Aug', 'Jul',
#                                        'Jun', 'May', 'Apr', 'Mar', 'Feb', 'Jan'])
#         self.assertEqual(self.notes, ['Do', 'Ti', 'La', 'So', 'Fa', 'Mi', 'Re',
#                                       'Do'])
#         self.assertEqual(self.multiples, [27, 24, 21, 18, 15, 12, 9, 6, 3, 0])

#     def test_2_J_custom_contains(self):
#         self.assertTrue(custom_contains(self.months, 'Jul'))
#         self.assertTrue(custom_contains(self.notes, 'Do'))
#         self.assertTrue(custom_contains(self.multiples, 27))

#         self.assertFalse(custom_contains(self.months, 'Hex'))
#         self.assertFalse(custom_contains(self.notes, 'Go'))
#         self.assertFalse(custom_contains(self.multiples, 30))

#     def test_2_K_custom_equality(self):
#         self.assertTrue(custom_equality(self.months, ['Jan', 'Feb', 'Mar', 'Apr',
#                                                       'May', 'Jun', 'Jul', 'Aug',
#                                                       'Sep', 'Oct', 'Nov', 'Dec']))
#         self.assertTrue(custom_equality(self.notes, ['Do', 'Re', 'Mi', 'Fa', 'So',
#                                                      'La', 'Ti', 'Do']))
#         self.assertTrue(custom_equality(self.multiples, [0, 3, 6, 9, 12, 15, 18,
#                                                          21, 24, 27]))

#         self.assertFalse(custom_equality(self.months, ['Jan', 'Feb', 'Mar', 'Apr',
#                                                       'May', 'Jun', 'Aug', 'Sep',
#                                                        'Oct', 'Nov', 'Dec']))
#         self.assertFalse(custom_equality(self.notes, self.notes[::-1]))
#         self.assertFalse(custom_equality(self.multiples, [0, 3, 6, 9, 12, 15, 18,
#                                                          21, 24]))

# if __name__ == '__main__':
#     unittest.main()