def best_score(a_dictionary):
    
    if  not a_dictionary:
        return None
    maxScore = max(a_dictionary,key=a_dictionary.get)
    return maxScore
