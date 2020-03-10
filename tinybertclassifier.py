#!/usr/bin/env python3
import tensorflow as tf
from transformers import *
import numpy as np
import pandas as pd
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv('IMDB_Dataset.csv', skiprows=1, header=None)
print(df.head())
df[1] = df[1].map({'positive': 1, 'negative': 0})
print(df.head())

df=df[:1500]

# Load tokenizer and tinyBERT
tokenizer = BertTokenizer.from_pretrained('bert-base-cased', do_lower_case=True)
config = BertConfig.from_json_file('./6L_768D_FinalModel/CoLA/config.json')
model = BertModel.from_pretrained('./6L_768D_FinalModel/CoLA/pytorch_model.bin', config=config)

tokenized = df[0].apply((lambda x: tokenizer.encode(x[0:511], add_special_tokens=True)))

max_len = 0
for i in tokenized.values:
    if len(i) > max_len:
        max_len = len(i)

padded = np.array([i + [0]*(max_len-len(i)) for i in tokenized.values])
np.array(padded).shape

attention_mask = np.where(padded != 0, 1, 0)
attention_mask.shape


input_ids = torch.tensor(padded)
attention_mask = torch.tensor(attention_mask)

with torch.no_grad():
    last_hidden_states = model(input_ids, attention_mask=attention_mask)

features = last_hidden_states[0][:,0,:].numpy()

labels = df[1]
train_features, test_features, train_labels, test_labels = train_test_split(features, labels)

lr_clf = LogisticRegression()
lr_clf.fit(train_features, train_labels)

print(lr_clf.score(test_features, test_labels))



