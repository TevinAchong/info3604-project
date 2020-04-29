#!/usr/bin/env python3
import nltk
import pandas as pd
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
nltk.download('stopwords')
from nltk.corpus import stopwords
import tensorflow as tf

flags = tf.flags

FLAGS = flags.FLAGS

flags.DEFINE_bool("remove_stop_words", False, "Whether to remove stop words")
flags.DEFINE_bool("stemming", False, "Stemming")



def remove_stop_words(df_dataset):
    # REMOVE STOP WORDS
    stop = stopwords.words('english')
    df_dataset['review'] = df_dataset['review'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    return df_dataset

def stemming(df_dataset):
    #Stemming
    stemmer = PorterStemmer()
    df_dataset['review'] = df_dataset['review'].apply(lambda x: ' '.join([stemmer.stem(word) for word in x.split()]))
    return df_dataset


# Read data from csv file
df_dataset = pd.read_csv('dataset/data.csv')

if FLAGS.remove_stop_words and FLAGS.stemming:
    df_dataset = remove_stop_words(df_dataset)
    df_dataset = stemming(df_dataset)
elif not FLAGS.remove_stop_words and FLAGS.stemming:
    df_dataset = stemming(df_dataset)
elif FLAGS.remove_stop_words and not FLAGS.stemming:
    df_dataset = remove_stop_words(df_dataset)
else:
    pass



# Creating the unique identifiers for the dataset
ids = []
for i in range(len(df_dataset)):
    ids.append(i)
pd_ids = pd.DataFrame(ids)
df_dataset.insert(0, "id", pd_ids)
# Converting sentiments from "positive" and "negative" to 1 and 0
df_dataset['sentiment'] = df_dataset['sentiment'].map({'positive': 1, 'negative': 0})


# Split into test and train set
df_train, df_test = train_test_split(df_dataset, test_size=0.2, shuffle=True)

# # Create new dataframes in the format required by BERT for train, dev data
df_bert = pd.DataFrame({'guid': df_train['id'],
                        'label': df_train['sentiment'],
                        'alpha': ['a'] * df_train.shape[0],
                        'text': df_train['review']})

# Split into test, dev
df_bert_train, df_bert_dev = train_test_split(df_bert, test_size=0.01)

# Create new dataframe for test data
df_bert_test = pd.DataFrame({'guid': df_test['id'],
                             'text': df_test['review']})

# Output tsv file, no header for train and dev
df_bert_train.to_csv('dataset/train.tsv', sep='\t', index=False, header=False)
df_bert_dev.to_csv('dataset/dev.tsv', sep='\t', index=False, header=False)
df_bert_test.to_csv('dataset/test.tsv', sep='\t', index=False, header=True)
