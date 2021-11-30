#!/bin/bash
echo "The data will be downloaded into temp/evaluate_raw"
echo "The text dataset will be built in temp/evaluate.bpri"
echo "The vectorized dataset will be built in temp/evaluate.pt"

python3 ../data/postDownloader.py

python3 ../data/data.py -compile

python3 ../model.py -vector -labeled 0