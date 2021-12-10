#!/bin/bash

echo "INSTALLING DEPENDENCIES"
pip install requests pandas torch transformers tqdm tensorflow numpy
echo "BEGINNING EVALUATION PIPELINE"
echo "GATHERING DATA"
python3 ../data/postDownloader.py
echo "PROCESSING DATA"
python3 ../data/data.py -compile
echo "VECTORING TEXT DATA"
python3 ../model.py -vector -unlabeled 0
echo "EVALUATING"
python3 ../Predict.py -test

