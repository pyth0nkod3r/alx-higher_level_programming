#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence = None
        return (None, sentence)
    else:
        return len(sentence), sentence[0]
