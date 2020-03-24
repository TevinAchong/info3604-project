from nltk.corpus import stopwords 
#from nltk.tokenize import word_tokenize ()

import pandas as pd
'''
run these lines if the first line of this code does not work!!!!!!
#import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
'''

df_train = pd.read_csv('imdb_train.csv')
df_test = pd.read_csv('imdb_test.csv')


stop = stopwords.words('english')

df_train['reviews_without_stopwords'] = df_train['review'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))


df_test['reviews_without_stopwords'] = df_test['review'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))


df_train.to_csv('train.csv', encoding='utf-8', index=False)
df_test.to_csv('test.csv', encoding='utf-8', index=False)

