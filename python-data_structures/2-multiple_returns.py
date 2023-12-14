def multiple_returns(sentence):
    length = len(sentence)
    
    if length == 0:
        first = sentence
        first = None
    else:
     first = sentence[0]
    return length,first