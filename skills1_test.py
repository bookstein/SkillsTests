import skills1 as sk1

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

print "Original number list: ", number_list
print "Original word list: ", word_list
word_functions = {
	"long_words": sk1.long_words,
	"word_len": sk1.word_lengths,
	"join_str": sk1.join_strings,
}

num_functions = {
	"odd": sk1.all_odd,
	"even": sk1.all_even,
	"sm": sk1.smallest,
	"larg": sk1.largest,
	"halve": sk1.halvesies,
	"sum_num": sk1.sum_numbers,
	"mult_num": sk1.mult_numbers,
	"avg": sk1.average,
}

#print out answers
for key in num_functions:
	test_num = num_functions[key](number_list)
	print key, test_num

for key in word_functions:
	test_word = word_functions[key](word_list)
	print key, test_word

#verify answers match expected answers