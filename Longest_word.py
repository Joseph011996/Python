#import sys

# import numpy as np
# import pandas as pd
# from sklearn import ...
print("Write your sentence below:")
sentence = input()

words = sentence.split()
#print(words)

longest_word = ""
longest_length = 0

for word in words:
    # Get the current word's length
    word_length = len(word)

    # Check if the current word is longer than the current longest
    if word_length > longest_length:
        longest_word = word
        longest_length = word_length

    # Print the longest word
print(longest_word)
