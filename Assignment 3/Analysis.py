key_words = ['boston', 'red', 'sox', 'new', 'york', 'yankees', 'world', 'series', 'champion', 'baseball']
from BostonRedSox import dict1
from NewYorkYankees import dict2

# differences = []
# for word in key_words:
#     difference = abs(dict1.get(word, 0) - dict2.get(word ,0))
#     if difference == 0:
#         differences.append(word)
#     differences.sort()
#     differences.reverse()
# print(differences)
""""determines which list has the word more frequently"""
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

print(which_list())

same_occurences = []
""""creates a list of words that appear the same number of times in each dictionary""""
for word in dict1:
    if word in dict2:
        same = dict1.get(word, 0) - dict2.get(word, 0)
        if same == 0:
            same_occurences.append(word)

print(same_occurences)
print(len(same_occurences))

""""output"""
# The word boston appears 58 more times on the Boston Red Sox page.
# The word red appears 191 more times on the Boston Red Sox page.
# The word sox appears 187 more times on the Boston Red Sox page.
# The word new appears 31 more times on the New York Yankees page.
# The word york appears 32 more times on the New York Yankees page.
# The word yankees appears 186 more times on the New York Yankees page.
# The word world appears 31 more times on the New York Yankees page.
# The word series appears 37 more times on the New York Yankees page.
# The word champion appears 1 more times on the Boston Red Sox page.
# The word baseball appears 1 more times on the Boston Red Sox page.
# ['outcome', '5th', 'usual', '200', 'competition', 'show', 'prove', 'step', '55', 'took', 'illustrious', 'decide', 'book', 'became', 'modern', 'california', 'arm', 'meeting', 'declined', 'expansion', '0', '1931', 'musical', 'links', 'teammates', 'potential', 'story', 'sat', 'people', '1-58261-767-8', 'scene', 'finishing', 'right', 'remained', 'toronto', 'flagship', 'murray', 'philadelphia', 'bob', 'plate', 'henderson', 'round', 'gathered', 'kid', 'station', 'arrival', 'bambino', 'ticket', 'nationally', 'shea', 'north', '7th', 'finance', 'clause', 'particularly', 'principal', 'stage', 'griffey', '11', 'largest', 'individuals', 'touch', 'intense', 'contrast', 'weekend', 'higher', 'sung', 'best-of-seven', 'eleven', 'active', 'frederic','chronological', '2–0', 'opened', 'subsequently', 'street', 'affiliations', '0-618-51748-0', 'bullpen', 'boone', 'suffering', '2009', 'office', 'could', '1953', 'stand', 'throwing', '15', 'talented', '0–3', 'termed', 'major', 'tragedy', 'torrez', 'twins', 'hip', 'wearing', 'man', 'stands', 'away', 'missed', 'serves', 'fell', '25th', '1945', 'spending', 'improved', 'johnson', 'jacoby', 'bless', 'bullpens', 'company', 'slugging', 'attempt', 'formerly', 'chants', '50', 'harvey', 'notes', 'separate', 'richard', 'phillies', 'twice', '1920s', 'newspaper', 'refer', 'deficit', 'original', 'moments', 'vastly', 'scouts', '175', 'signs', 'koufax', '1910s', 'built', 'bad', 'few', 'standings', 'depth', 'replaced', 'rebuilt', 'left-field', 'consistently', 'seattle', '1932', 'annual', 'holds', 'northeastern', 'committed', 'hits', 'insurrectos', 'controversial', 'owner', 'base', '86', 'outscoring', 'high-profile', 'those', 'catching', 'heated', 'russell', 'batter', 'given', 'within','glenn', 'national', 'san', 'should', 'dramatic', 'challenge', 'stanley', 'nl', '0–2', 'reasons', 'pick', '1906', 'eliminated', 'white', 'room', 'choice', 'frick', '95–67', 'specifically', 'halfway', 'points', 'produced', 'bleachers', 'surpassing', 'serving', 'age', 'ken', 'curse', 'giving', 'charles', 'historical', 'subject', '1963', 'jays', 'franchise', 'putting', 'further', 'bernie', '120', 'commissioner', 'commentary', 'chant', 'achieved', 'centennial', 'revived', 'providing', 'surrounding', 'western', 'buck', 'diamondbacks', 'grandfather', '14-game', 'season-ending', 'jersey', 'appear', 'though', 'renamed', 'earth', 'wife', 'tigers', 'struck', 'entered', 'ultimately', 'antagonized', 'television', 'external', 'met', 'behind', 'frommer', 'organization', 'doug', 'best', 'released', 'far', 'states', 'deciding', 'long', 'globe', 'instrumental', 'wrigley', '9th', 'qualified', 'index', 'removed', '1992', 'recent', 'posting', 'revamped', 'remembered','finally', 'tommy', 'god', 'control', 'once', 'expectations', 'vice', 'use', 'struggling', 'among', 'during', 'catch', 'developed', 'sometimes', 'add', 'months', 'midway', 'swing', '1902', 'eight', 'no-hit', 'be', 'colorado', 'taunt', 'set', 'telecast', '80', 'connected', 'least', 'maryland', '7–0', 'arizona', '34', 'lineup', 'houghton', 'ii', 'repeat', 'incident', 'job', "park's", '1965', 'changed', 'aaron', 'similar', 'publishing', 'dimensions', 'milwaukee', 'core', 'refused', '4-year', 'style', 'discovered', 'fill', 'carlos', 'selection', 'notably', 'performing', 'sad', 'attitude', 'helm', 'anniversary', 'stout', 'less', 'marked', '1980', 'mifflin', '16', 'allowed', 'critics', 'poor', 'veterans', 'reversing', 'allen', 'combination', 'vs', 'plans', 'yankees–red', 'seven', '2002', 'sandy', 'research', 'demeaning', 'much', 'returning', '2013–14', 'famers', 'torn', 'nearly', 'james', 'celebrate', 'million', 'getting', 'deep', 'extensive']

#2009, jacoby 