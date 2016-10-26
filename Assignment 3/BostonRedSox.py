import wikipedia
import pickle

team = "Boston Red Sox"
source = wikipedia.page("Boston Red Sox")

# print(wikipedia.summary(team, sentences=3))

#x = wikipedia.search(team, results=1000)
#search has a cap at 500
#print(len(x))


# # Load data from a file (will be part of your data processing script)
file_name = "Boston Red Sox Data.pickle"
input_file = open(file_name,'br')
reloaded_copy_of_texts = pickle.load(input_file)

def word_list(page):
    hist = {}
    for line in source.content:
        for word in line.split:
        # for word in line.split():
            word = word.lower()
            hist[word] = hist.get(word,0)+1
    return hist

print(word_list(team))

#print(source.content)

