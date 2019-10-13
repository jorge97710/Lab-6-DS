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




