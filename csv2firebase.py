#!/usr/bin/env python3
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import csv

cred = credentials.Certificate("final-project-data-collection-firebase-adminsdk-5y7ve-63cb93e768.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()
doc_ref = store.collection(u'reviews')

with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (row['sentiment'] == 'positive'):
            doc_ref.add({u'review':row['review'], 'sentiment':1, u'translated':False, u'trini_translation':u''})
        else:
            doc_ref.add({u'review':row['review'], 'sentiment':0, u'translated':False, u'trini_translation':u''})




