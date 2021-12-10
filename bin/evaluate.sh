#!/bin/bash

echo "INSTALLING DEPENDENCIES"
pip install requests datetime traceback time json sys pandas torch transformers tqdm simplejson.errors tensorflow numpy
echo "BEGINNING EVALUATION PIPELINE"
echo "GATHERING DATA"
python3 ../data/postDownloader.py
echo "PROCESSING DATA"
python3 ../data/data.py -compile
echo "VECTORING TEXT DATA"
python3 ../model.py -vector -unlabeled 0
echo "EVALUATING"
python3 ../Predict.py -test

