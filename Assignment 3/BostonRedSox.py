import wikipedia
import pickle

team = "Boston Red Sox"
source = wikipedia.page("Boston Red Sox")

# print(type(source))
# print(wikipedia.summary(team, sentences=3))

#x = wikipedia.search(team, results=1000)
#search has a cap at 500
#print(len(x))


# # Load data from a file (will be part of your data processing script)
file_name = "Boston Red Sox Data.pickle"
input_file = open(file_name,'br')
reloaded_copy_of_texts = pickle.load(input_file)


#print(reloaded_copy_of_texts)

def word_list(page):
    hist = {}
    for word in page.split():
        word = word.lower()
        hist[word] = hist.get(word,0)+1
    return hist

#print(word_list(reloaded_copy_of_texts))
dict1 = word_list(reloaded_copy_of_texts)

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)
#print(different_words(hist))
#print(different_words(reloaded_copy_of_texts))

stopwords = ['a', 'the', 'in', 'of', 'the', 'is', 'are', 'am', 'at', 'but', 'by', 'was', 'to', 'and', 'for', 'as', 'with', 'on', 'that', 'from', 'were', 'his', 'had', 'their', '===']

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
    print('Total number of words:', total_words(dict1))
    print('Total numer of different words:', different_words(dict1))
    print('The most common words are', common_wordlist[:10])
    print("The word 'boston' appears", dict1.get('boston',0), "times.")
    print("The word 'red' appears", dict1.get('red',0), "times.") 
    print("The word 'sox' appears", dict1.get('sox',0), "times.") 
    print("The word 'new' appears", dict1.get('new',0), "times.") 
    print("The word 'york' appears", dict1.get('york',0), "times.") 
    print("The word 'yankees' appears", dict1.get('yankee' or 'yankees',0), "times.")
    print("The word 'world' appears", dict1.get('world',0), "times.") 
    print("The word 'series' appears", dict1.get('series',0), "times.")
    print("The word 'champion' appears", dict1.get('champion',0), "times.") 
    print("The word 'baseball' appears", dict1.get('baseball',0), "times.") 

main()

# import nltk

# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# sentence = 'Software Design is my favorite class because learning Python is so cool!'
# score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)

# import numpy as np
# from sklearn.manifold import MDS
# import matplotlib.pyplot as plt

# # these are the similarities computed from the previous section
# S = np.asarray([[1., 0.90850572, 0.96451312, 0.97905034, 0.78340575],
#     [0.90850572, 1., 0.95769915, 0.95030073, 0.87322494],
#     [0.96451312, 0.95769915, 1., 0.98230284, 0.83381607],
#     [0.97905034, 0.95030073, 0.98230284, 1., 0.82953109],
#     [0.78340575, 0.87322494, 0.83381607, 0.82953109, 1.]])

# # dissimilarity is 1 minus similarity
# dissimilarities = 1 - S

# # compute the embedding
# coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)
# plt.scatter(coord[:, 0], coord[:, 1])

# # Label the points
# for i in range(coord.shape[0]):
#     plt.annotate(str(i), (coord[i, :]))

# plt.show()