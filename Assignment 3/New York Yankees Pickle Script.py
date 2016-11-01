# Save data to a file (will be part of your data fetching script)
data_dump = source.content
f = open("New York Yankees Data.pickle",'wb')
pickle.dump(data_dump,f)
f.close()