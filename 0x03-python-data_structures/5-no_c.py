#!/usr/bin/python3

def no_c(my_string):
    word = []
    word.append(my_string)
    unwanted = ['c', 'C']
    for each_word in word:
        new_word = ""
        for char in each_word:
            if char not in unwanted:
                new_word += char
        return new_word
