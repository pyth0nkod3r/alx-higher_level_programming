#!/usr/bin/python3

def uppercase(str):
    result = ""
    for letter in str:
        if ord(letter) in range(97, 124):
            result += chr(ord(letter) - 32)
        else:
            result += chr(ord(letter))
    print("{}".format(result))
