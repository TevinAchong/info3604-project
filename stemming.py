import pandas as pd 
from nltk.stem import PorterStemmer

#stemmer = SnowballStemmer("english")
stemmer = PorterStemmer()

df_test = pd.read_csv('imdb_test.csv')

df_test['stemmed_review'] = df_test['review'].apply(lambda x: ' '.join([stemmer.stem(word) for word in x.split()]))# Stem every word.
df_test = df_test.drop(columns=['review'])

df_test.to_csv('test.csv', encoding='utf-8', index=False)


#print(stemmer.stem("gone"))