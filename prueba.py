
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import string
import nltk
#nltk.download('averaged_perceptron_tagger')
#nltk.download('brown')
import numpy
import numpy as np
import pandas as pd
import re, operator
from os import path
from PIL import Image
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

# nltk.download('stopwords')
stop_words = stopwords.words('english')
cachedStopWords = stopwords.words("english")



data = pd.read_csv('GrammarandProductReviews.csv')
print(data['reviews.text'])


for item in data['reviews.text'].tolist():
    print(item)

with open('reviews.txt', 'w', encoding='utf-8') as filehandle:
    for listitem in data['reviews.text'].tolist():
        filehandle.write('%s\n' % listitem)


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
def remove_urls(vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return (vTEXT)


#
#
# file1 = open("reviews_limpio.txt", "w")  # append mode
# with open('reviews.txt', errors='ignore') as txt_file:
#     print("start revs")
#     for line in txt_file:
#         # process the line
#         # print (line)
#         line = line.lower()
#         line = remove_emoji(line)
#         line = remove_urls(line)
#         line = line.translate(str.maketrans("?!,$.@", 6 * " ", string.punctuation))
#         line= re.sub(' +', ' ', line)
#         regex = re.compile('[^a-zA-Z]')
#         # First parameter is the replacement, second parameter is your input string
#         line=  regex.sub(' ', line)
#         line = ' '.join([word for word in line.split() if word not in cachedStopWords])
#         file1.write(line + " \n")
#     pass
# file1.close()
# print("done revs")

results = []

import re, operator
filePath = "/Users/xah/web/xahlee_info/python/python_word_frequency.html"
 # keys are words, vals are occurance frequency
freqlist = {}
inF = open("reviews_limpio.txt", "r", encoding="utf-8")
s = inF.read()
inF.close()
s = s.lower()
wordlist = re.split(r"\W", s)
for wd in wordlist:
    if wd in freqlist:
        freqlist[wd] = freqlist[wd] + 1
    else:
        freqlist[wd] = 1
for k, v in sorted(freqlist.items(), key=operator.itemgetter(1), reverse=True):
    # print(str(v) + " → " + k)
    results.append([k, v])
df = pd.DataFrame(results, columns=['Word', 'Freq'])
# print(df.iloc[1:])
ndf = df.iloc[1:]
print(ndf.head(20))
fndf = ndf.head(20)
fndf.plot(kind='bar', x='Word', y='Freq')
plt.show()

from textblob import TextBlob


f = open('reviews_limpio.txt', 'r')
x = f.readlines()
f.close()
#print (x)
results = []

for item in x:
    blob = TextBlob(str(item))
    for sentence in blob.sentences:
        #print(sentence.sentiment.polarity)
        results.append([item,sentence.sentiment.polarity])

df = pd.DataFrame(results, columns=['Review', 'Score'])

print("done")
print(df.head(20))



from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)


def show_wordcloud(data):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40,
        scale=3,
        random_state=1
    ).generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')


    plt.imshow(wordcloud)
    plt.show()

show_wordcloud(s)
