key_words = ['boston', 'red', 'sox', 'new', 'york', 'yankees', 'world', 'series', 'champion', 'baseball']
from BostonRedSox import dict1
from NewYorkYankees import dict2

def difference_in_lists():
    differences = []
    for word in key_words:
        differece = abs(dict1.get(word, 0) - dict2.get(word ,0))
        differences.append(word)
    difference.sort()
    difference.reverse()
    return difference

print(difference_in_lists())

greatest_difference_wordlist = differences

def which_list():
    for word in key_words:
        net = dict1.get(word, 0) - dict2.get(word, 0)
        if net > 0:
            print("The word", word, "appears", net, "more times on the Boston Red Sox page.")
        if net < 0:
            print("The word", word, "appears", abs(net), "more times on the New York Yankees page.")
        if net == 0:
            print("Wow! The word", word, "appears on both pages the same number of times!")
    return


def analysis():
    print(which_list)
    print('The highest frequency different words are', greatest_difference_wordlist[:10])


same_occurences = []

for word in dict1:
    if word in dict2:
        same = dict1.get(word, 0) - dict2.get(word, 0)
        if same == 0:
            same_occurences.append(word)

print(same_occurences)

analysis()