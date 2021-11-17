###PYTHON FILE TO DEFINE DATABASE OBJECT WHICH CAN EITHER LOAD WHOLE DATASET INTO LIST OR BE ITERABLE###
###SAM CHANOW###
import torch
# Create a dataset object and pass in a list of files. The dataset is iterable and if you iterate over it it will
# grab every line and return it. It will not parse the data by default but, but if a parsing function is passed in it will utilize it


class Dataset:
    # If the data is in .pt file format and needs to be loaded file by file with torch, then set
    # tensor_data = True
    def __init__(self, files, parse_f=lambda x: x, tensor_data=False):
        self.tensor_data = tensor_data
        if not tensor_data:
            self.files = files
            self.fp = open(files[0], 'r')
            self.curr = 0
            self.parse_f = parse_f
        else:
            self.files = files
            self.curr = -1
            self.parse_f = parse_f

    def __iter__(self):
        return self

    def __next__(self):
        if not self.tensor_data:
            nextL = self.fp.readline()
            if not nextL:
                self.curr += 1
                if self.curr >= len(self.files): raise StopIteration
                self.fp = open(self.files[self.curr], 'r')
                nextL = self.fp.readline()
                return self.parse_f(nextL)
            else:
                return self.parse_f(nextL)
        else:
            self.curr += 1
            if self.curr >= len(self.files): raise StopIteration
            return self.parse_f(torch.load(self.files[self.curr]))


# These are two parsing functions available for use with the dataset class
def parseBPRI(posts):  # Given a string of posts in BPRI format, return s a list with the label and list of posts
    bpri = posts.split('//POSTDATACOMPILED//')
    bpri[1] = bpri[1].split('/ENDPOST/')
    return bpri


def parseBVBPRI(data):  # Given a string that is a Bert Vectorized data with a label
    pass


# D = Dataset(['data/compiled-datasets/BPRI-POSTSPLIT/BPRI00.bpri', 'data/compiled-datasets/BPRI-POSTSPLIT/BPRI01.bpri'], parseBPRI)
# D = iter(D)

# for bpri in D:
    # print(bpri)

#D = Dataset(['data/compiled-datasets/BVBPRI/BVBPRI0.pt', 'data/compiled-datasets/BVBPRI/BVBPRI1.pt'], tensor_data=True)
#D = iter(D)

#for day in D:
    #print(day[0])
