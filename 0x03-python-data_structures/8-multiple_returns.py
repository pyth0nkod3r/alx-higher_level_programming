#!/usr/bin/python3

def multiple_returns(sentence):
    """
    This function takes a sentence as input.
    If the sentence is an empty string, it returns a tuple with a None value and the same empty string.
    If the sentence is not an empty string, it returns a tuple with the length of the sentence and the first character of the sentence.
    """

    # Check if the input sentence is an empty string
    if sentence == "":
        # If it is, set the sentence variable to None
        sentence = None
        # Return a tuple with a None value and the same empty string
        return (None, sentence)
    # If the input sentence is not an empty string
    else:
        # Get the length of the sentence
        length = len(sentence)
        # Get the first character of the sentence
        first_char = sentence[0]
        # Return a tuple with the length of the sentence and the first character of the sentence
        return (length, first_char)
