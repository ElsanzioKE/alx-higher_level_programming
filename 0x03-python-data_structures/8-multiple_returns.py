#!/usr/bin/python3
def multiple_returns(sentence):

    """returns a tuple with the lrnght of a string"""

    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
