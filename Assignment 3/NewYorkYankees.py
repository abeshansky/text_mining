import wikipedia

team = "New York Yankees"

print(wikipedia.summary(team, sentences=3))


x = wikipedia.search(team, results=1000)


print(len(x))