###MODEL CLASS FOR the BPRI DATASET TRAINING###
###SAM CHANOW RYAN METZ###

import dataset
import torch
from transformers import BertTokenizer, BertModel, BertConfig
from time import sleep
from tqdm import tqdm
import sys


# This function will use BERT to vectorize a datset and return a new Dataset
# This function expects a BPRI parsed dataset
def build_vector_data(raw_data, start_tok=0):  # raw_data is a dataset object, and this will make a vectorized dataset for the model
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
        label = post[0]
        posts = post[1]

        v = [label, []]

        for s in tqdm(posts):
            post_v = tokenizer(s, truncation=True, return_tensors="pt", padding=True)
            outputs = model(**post_v)
            data = outputs.last_hidden_state[0][0]
            v[1].append(data)

        torch.save(v, 'data/compiled-datasets/BVBPRI/BVBPRI' + str(f_n) + '.pt')
        #if f_n > 1: break;


# This function will clean a string of data
def clean(sentence):
    pass


class Model:
    def __init__(self):
        pass

    def train(self, train_d):
        pass

    def test(self, test_d):
        pass

    def evaluate(self, data_unlabeled):
        pass


if __name__ == "__main__":
    if (len(sys.argv) > 1) and (sys.argv[1] == '-vector'):
        D = dataset.Dataset(['data/compiled-datasets/BPRI-POSTSPLIT/BPRI00.bpri', 'data/compiled-datasets/BPRI-POSTSPLIT/BPRI01.bpri', 'data/compiled-datasets/BPRI-POSTSPLIT/BPRI02.bpri'], dataset.parseBPRI)
        build_vector_data(D, int(sys.argv[2]))
    if (len(sys.argv) > 1) and (sys.argv[1] == '-load'):
        l = torch.load('data/compiled-datasets/BVBPRI/BVBPRI0.pt')
        print(l[1][0])
