import numpy as nmp 
import pandas as pd
import os
import seaborn as sea
import matplotlib.pyplot as plt
import re


data = pd.read_csv('GrammarandProductReviews.csv')
print(data.head)
sea.countplot(data['reviews.rating'])
plt.show()
sea.countplot(data['reviews.didPurchase'])
plt.show()
sea.countplot(data['reviews.userCity'])
plt.show()
sea.countplot(data['reviews.userProvince'])
plt.show()
plt.hist(seq_lens, bins=50)
plt.show()
sea.countplot(data['seq_lens'])
plt.show()
plt.matshow(data.corr())
plt.show()




##Elimina los emojis de strings 
def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

##quita los urls de los textos
##Fuente: https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python
def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)


def lower(text):
    return text.lower()


def remove_punctuation(text):
    punct = string.punctuation
    trantab = str.maketrans(punct, len(punct)*' ')
    return text.translate(trantab)


remove_emoji(data)
lowe(data)
remove_punctuation(data)
data.translate(str.maketrans("?!,$.@", 6*" ", string.punctuation))

#print(data.head)
str = str(data)
#print(data)
data = str.lower()
print (data)

all_text = ''.join([c for c in data if c not in punctuation])
reviews_split = all_text.split("\n")
from collections import Counter
all_text2 = ' '.join(reviews_split)
# create a list of words
words = all_text2.split()
# Count all the words using Counter Method
count_words = Counter(words)

total_words = len(words)
sorted_words = count_words.most_common(total_words)
vocab_to_int = {w:i+1 for i, (w,c) in enumerate(sorted_words)}
print ('Number of reviews :', len(reviews_split))
reviews_int = []
for data in reviews_split:
    r = [vocab_to_int[w] for w in data.split()]
    reviews_int.append(r)
print (reviews_int[0:3])

import numpy as nmp 
#import nltk
#nltk.download('all')
import pandas as pd
import os
import seaborn as sea
import matplotlib.pyplot as plt
import re
from string import punctuation
from textblob import TextBlob



data = pd.read_csv('GrammarandProductReviews.csv')
#print(data.head)
str = str(data)
for col in data.columns: 
    print(col)
#reviews.doRecommend
df = pd.DataFrame(data,columns=['reviews.text'])
print("DF", df)
print (', '.join(df))
df = ', '.join(df)
#df = str.lower()
print("STRING CONVERT",df)
print("END CONVERT")
#print(data(reviews.doRecommend))
#print(data)
#data = str.lower()
#data = ''.join(data)
text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''
from textblob import TextBlob

blob = TextBlob(text)
print(blob)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]
print(blob.tags)
blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])
print(blob.noun_phrases)
for sentence in blob.sentences:
    print(sentence.sentiment.polarity)


blob.translate(to="es")  # 'La amenaza titular de The Blob...'



