#!/usr/bin/env python3
import tensorflow as tf
from transformers import *
import numpy as np
import pandas as pd
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import nltk
nltk.download('stopwords')


# Load dataset
df = pd.read_csv('IMDB_Dataset.csv', skiprows=1, header=None)
print(df.head())
df[1] = df[1].map({'positive': 1, 'negative': 0})
#remove stop words
stop = stopwords.words('english')
df[0] = df[0].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
print(df.head())

#df=df[:10000]

# Load tokenizer and tinyBERT
tokenizer = BertTokenizer.from_pretrained('../bert-base-cased', do_lower_case=True)
config = BertConfig.from_json_file('../config_4l.json')
model = BertModel.from_pretrained('../pytorch_model_4l.bin', config=config)
tokenized = df[0].apply((lambda x: tokenizer.encode(x[0:511], add_special_tokens=True)))

max_len = 0
for i in tokenized.values:
    if len(i) > max_len:
        max_len = len(i)

padded = np.array([i + [0]*(max_len-len(i)) for i in tokenized.values])
np.array(padded).shape

attention_mask = np.where(padded != 0, 1, 0)
attention_mask.shape

input_ids = torch.tensor(padded).cpu()
attention_mask = torch.tensor(attention_mask).cpu()

with torch.no_grad():
    last_hidden_states = model(input_ids, attention_mask=attention_mask)

features = last_hidden_states[0][:,0,:].cpu().data.numpy()

labels = df[1]
train_features, test_features, train_labels, test_labels = train_test_split(features, labels)

lr_clf = LogisticRegression()
lr_clf.fit(train_features, train_labels)

print(lr_clf.score(test_features, test_labels))