#!/usr/bin/env bash

prepare_data () {
    rm -r *.tsv
    python prepare_data.py
}

#check if BERT repo is cloned locally, if not download.
if ! [[ -d bert ]]
then
    echo "BERT not present. Cloning..."
    git clone --quiet https://github.com/google-research/bert.git
fi

#check if dataset directory is present
if ! [[ -d dataset ]]
then
    mkdir dataset
fi

#check for csv file
if ! [[ -f /dataset/data.csv ]]
then
    wget -q --no-check-certificate 'https://docs.google.com/uc?export=download&id=1Ck5oCZK6Ki3ByzdY0-poYENXZYpQUaCb' -O data.csv
    mv data.csv dataset/
fi

#check for tsv file
if  [[ ! -f /dataset/train.tsv]] ||  [[ ! -f /dataset/dev.tsv ]] || [[ ! -f test.tsv ]]
then
    prepare_data
fi
