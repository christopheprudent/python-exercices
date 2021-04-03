import collections

sentence = 'a very long sentence with many words, and splited as word to count them, and print the result of occurences for each!'
letter_count = collections.Counter(sentence)
print(letter_count)

word_count = collections.Counter(sentence.split(' '))
print(word_count)
