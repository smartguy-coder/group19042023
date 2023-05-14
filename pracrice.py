text = 'ekjhgjkdfh kludfgk fdhgkdfh gkdflukgfdklg dFFFfklhgkdfhkg' * 10000
# text = text.lower()

unique_letters = set(text)
print(unique_letters)

dict_counter = dict.fromkeys(unique_letters, 0)
print(dict_counter)

# for letter in unique_letters:
for letter in dict_counter:
    dict_counter[letter] = text.count(letter)

print(dict_counter)

# for letter in text:
#     dict_counter[letter] += 1
#
# print(dict_counter)