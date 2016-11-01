key_words = ['boston', 'red', 'sox', 'new', 'york', 'yankees', 'world', 'series', 'champion', 'baseball']
from BostonRedSox import dict1
from NewYorkYankees import dict2

def analysis():
    for word in key_words:
        net = dict1.get(word, 0) - dict2.get(word, 0)
        if net > 0:
            print("The word", word, "appears", net, "more times on the Boston Red Sox page.")
        if net < 0:
            print("The word", word, "appears", abs(net), "more times on the New York Yankees page.")
        if net == 0:
            print("Wow! The word", word, "appears on both pages the same number of times!")
    for word in dict1 and dict2:
        same_occurences = []
        net = dict1.get(word, 0) - dict2.get(word, 0)
        if net == 0:
            same_occurences.append(word)
        return same_occurences
analysis()