word = "Holberton"
word_first_3 = word[:3]
print("First 3 letters: {}".format(word_first_3))
word_last_2 = word[-2:]
print("Last 2 letters: {}".format(word_last_2))
middle_index = len(word) // 2
middle_word = word[middle_index - 1:middle_index + 2]
print("Middle word: {}".format(middle_word))
