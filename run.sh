#!/usr/bin/env bash

while getopts m:r:s:l: aflag; do
    case $aflag in
            m) model=$OPTARG;;
            r) remove_stop_words=$OPTARG;;
            s) stemming=$OPTARG;;
            l) max_seq_len=$OPTARG;;
    esac
done

#check for output directory
if [[ ! -d bert_output ]]
then
    mkdir bert_output
fi

#check for virtualenv
if [[ ! -f venv/bin/activate ]]
then
    echo "Making venv"
    mkdir venv
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
else
    source venv/bin/activate
fi

prepare_data () {
    if [[ -f /dataset/*.tsv ]]
    then
        rm -r *.tsv
    fi
    if  [[ ! -x prepare_data.py ]]
    then
        chmod +x prepare_data.py
    fi
    if [[ ${remove_stop_words} == "True" ]] && [[ ${stemming} == "True" ]]
    then
        ./prepare_data.py remove_stop_words=True stemming=True
    elif [[ ${remove_stop_words} == "False" ]] && [[ ${stemming} == "True" ]]
    then
        ./prepare_data.py remove_stop_words=False stemming=True
    elif  [[ ${remove_stop_words} == "True" ]] && [[ ${stemming} == "False" ]]
    then
        ./prepare_data.py remove_stop_words=True stemming=False
    else
        ./prepare_data.py
    fi
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

#prepare data
prepare_data

#check for models directory
if ! [[ -d models ]]
then
    mkdir models
fi

#check for model
if [[ ${model} == "bert" ]]
then
    if [[ ! -d models/bert ]]
    then
        echo "Downloading model..."
        wget -q https://storage.googleapis.com/bert_models/2018_10_18/cased_L-12_H-768_A-12.zip -O cased.zip
        mkdir models/bert
        unzip cased.zip -d models/bert/
        rm -r cased.zip
        mv models/bert/cased_L-12_H-768_A-12/* models/bert/
        mv models/bert/bert_config.json models/bert/config.json
    fi
elif [[ ${model} == "tiny-bert" ]]
then
    if [[ ! -d models/tiny-bert ]]
    then
        echo "Downloading model..."
        wget -q --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=11hAu7t52tKbd8c3ck4t_DlTs_fGy50PG' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=11hAu7t52tKbd8c3ck4t_DlTs_fGy50PG" -O tiny-bert.zip && rm -rf /tmp/cookies.txt
        mkdir models/tiny-bert
        unzip tiny-bert.zip -d models/tiny-bert/
        rm -r tiny-bert.zip
        mv models/tiny-bert/2nd_General_TinyBERT_4L_312D/* models/tiny-bert/
    fi
elif [[ ${model} == "bert-tiny" ]]
then
    if [[ ! -d models/bert-tiny ]]
    then
        echo "Downloading model..."
        wget -q --no-check-certificate 'https://docs.google.com/uc?export=download&id=1C56uju9E5WholSfK9-jtsS17LX3nJfdL' -O bert-tiny.zip
        mkdir models/bert-tiny
        unzip bert-tiny.zip -d models/bert-tiny/
        rm -r bert-tiny.zip
        mv models/bert-tiny/bert_config.json models/bert-tiny/config.json
        fi
fi

cd bert

start=`date +%s`
python3 run_classifier.py --task_name=cola --do_train=true --do_eval=true --data_dir=./../dataset --vocab_file=./../models/${model}/vocab.txt --bert_config_file=./../models/${model}/config.json --init_checkpoint=./../models/${model}/bert_model.ckpt --max_seq_length=${max_seq_len} --train_batch_size=2 --learning_rate=2e-5 --num_train_epochs=3.0 --output_dir=./../bert_output/ --do_lower_case=False --save_checkpoints_steps 1000
end=`date +%s`
runtime=$((end-start))
echo "$runtime"