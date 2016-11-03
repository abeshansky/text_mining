import wikipedia
import pickle
import string
team = "New York Yankees"
source = wikipedia.page("New York Yankees")

# # Load data from a file (will be part of your data processing script)
file_name = "New York Yankees Data.pickle"
input_file = open(file_name,'br')
reloaded_copy_of_texts = pickle.load(input_file)

def word_list(page):
    hist = {}

    strippables = string.punctuation + string.whitespace
    for word in page.split():
        word = word.strip(strippables)
        word = word.lower()

        hist[word] = hist.get(word,0)+1
    return hist

#print(word_list(reloaded_copy_of_texts))
dict2 = word_list(reloaded_copy_of_texts)

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)
#print(different_words(hist))
#print(different_words(reloaded_copy_of_texts))

stopwords = ['a', 'the', 'in', 'of', 'the', 'is', 'are', 'am', 'at', 'but', 'by', 'was', 'to', 'and', 'for', 'as', 'with', 'on', 'that', 'from', 'were', 'his', 'had', 'their', '===' , '', 'they']

def most_common(hist):
    temp = []
    for word, frequency in hist.items():
        temp.append((frequency, word))
        if word in stopwords:
            temp.remove((frequency, word))
    temp.sort()
    temp.reverse()
    return temp

common_wordlist = most_common(word_list(reloaded_copy_of_texts))

def main():
    print('Total number of words:', total_words(dict2))
    print('Total numer of different words:', different_words(dict2))
    print('The most common words are', common_wordlist[:10])
    print("The word 'boston' appears", dict2.get('boston',0), "times.")
    print("The word 'red' appears", dict2.get('red',0), "times.") 
    print("The word 'sox' appears", dict2.get('sox',0), "times.") 
    print("The word 'new' appears", dict2.get('new',0), "times.") 
    print("The word 'york' appears", dict2.get('york',0), "times.") 
    print("The word 'yankees' appears", dict2.get('yankees',0), "times.")
    print("The word 'world' appears", dict2.get('world',0), "times.") 
    print("The word 'series' appears", dict2.get('series',0), "times.")
    print("The word 'champion' appears", dict2.get('champion',0), "times.") 
    print("The word 'baseball' appears", dict2.get('baseball',0), "times.")

import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentence = reloaded_copy_of_texts
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)

if __name__ =='__main__':
    main()
    #print(dict2)

# Total number of words: 11057
# Total numer of different words: 2425
# The most common words are [(242, 'yankees'), (115, 'series'), (80, 'world'),
# (78, 'team'), (76, 'new'), (64, 'season'), (61, 'league'),
# (57, 'games'), (52, 'first'), (48, 'home')]
# The word 'boston' appears 18 times.
# The word 'red' appears 41 times.
# The word 'sox' appears 42 times.
# The word 'new' appears 76 times.
# The word 'york' appears 47 times.
# The word 'yankees' appears 242 times.
# The word 'world' appears 80 times.
# The word 'series' appears 115 times.
# The word 'champion' appears 2 times.
# The word 'baseball' appears 28 times.
# {'neu': 0.837, 'neg': 0.065, 'pos': 0.099, 'compound': 0.9999}