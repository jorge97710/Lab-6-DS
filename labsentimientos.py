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




