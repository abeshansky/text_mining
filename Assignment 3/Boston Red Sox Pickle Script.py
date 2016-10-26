import wikipedia
import pickle
team = "Boston Red Sox"
source = wikipedia.page("Boston Red Sox")
# Save data to a file (will be part of your data fetching script)
data_dump = source.content
f = open("Boston Red Sox Data.pickle",'wb')
pickle.dump(data_dump,f)
f.close()