#!/usr/bin/python3

def no_c(my_string):
    word = []
    word.append(my_string)
    for char in word:
        if char == 'c' or char == 'C':
            word.remove(char)
    new_str = ''
    for element in word:
        new_str += element
    return element
