import numpy as nmp 
import pandas as pd
import os
import seaborn as sea
import matplotlib.pyplot as plt
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
