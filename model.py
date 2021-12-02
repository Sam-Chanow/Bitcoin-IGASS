###MODEL CLASS FOR the BPRI DATASET TRAINING###
###SAM CHANOW RYAN METZ###

import dataset
import torch
from transformers import BertTokenizer, BertModel, BertConfig
from time import sleep
from tqdm import tqdm
import sys
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


# This function will use BERT to vectorize a datset and return a new Dataset
# This function expects a BPRI parsed dataset
def build_vector_data(raw_data, start_tok=0, unlabeled=False):  # raw_data is a dataset object, and this will make a vectorized dataset for the model
    # Vector data writes the vectorized data to a file and returns a dataset object pointing to that file

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    config = BertConfig.from_pretrained('bert-base-uncased', output_hidden_states=True)
    model = BertModel.from_pretrained('bert-base-uncased', config=config)

    # vector data to store to file
    f_n = -1

    # We are not gonna split by sentence right now, insteaad we will split by post, we may change this later
    for post in iter(raw_data):
        f_n += 1
        if f_n < start_tok: continue
        # The line above lets you pickup at a different file
        v = []
        if not unlabeled:
            label = post[0]
            posts = post[1]
            v = [label, []]
        else:
            posts = post

        for s in tqdm(posts):
            post_v = tokenizer(s, truncation=True, return_tensors="pt", padding=True)
            outputs = model(**post_v)
            data = outputs.last_hidden_state[0][0]
            v[1].append(data)

        if not unlabeled:
            torch.save(v, 'data/compiled-datasets/BVBPRI/BVBPRI' + str(f_n) + '.pt')
        else:
            torch.save(v, 'data/temp/evaluate.pt')
        #if f_n > 1: break;


def average_tensors(data):
    # Takes in a list of tensors, data
    #average them all together and return a single tensor
    num = len(data)
    sum = 0

    for t in data:
        sum += t

    return sum/num


def build_labels(label):
    if label == 'UP ': return [1,0]
    elif label == 'DOWN ': return [0,1]
    else:
        print("FUCK YOU")


if __name__ == "__main__":
    if (len(sys.argv) > 2) and (sys.argv[1] == '-vector'):
        if sys.argv[2] == '-labeled':
            D = dataset.Dataset(['data/compiled-datasets/BPRI-POSTSPLIT/BPRI00.bpri', 'data/compiled-datasets/BPRI-POSTSPLIT/BPRI01.bpri', 'data/compiled-datasets/BPRI-POSTSPLIT/BPRI02.bpri'], dataset.parseBPRI)
            build_vector_data(D, int(sys.argv[3]))
        elif sys.argv[2] == '-unlabeled':
            input_file = input("Dataset path: ")
            D = dataset.Dataset([input_file], dataset.unlabeled_parseBPRI)
            build_vector_data(D, int(sys.argv[3]), unlabeled=True)
    if (len(sys.argv) > 1) and (sys.argv[1] == '-load'):
        l = torch.load('data/compiled-datasets/BVBPRI/BVBPRI0.pt')
        print(l[1][0])
