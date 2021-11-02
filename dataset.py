###PYTHON FILE TO DEFINE DATABASE OBJECT WHICH CAN EITHER LOAD WHOLE DATASET INTO LIST OR BE ITERABLE###
###SAM CHANOW###

# Create a dataset object and pass in a list of files. The dataset is iterable and if you iterate over it it will
# grab every BPRI formatted line and return it as a parsed list (over all the files)
class Dataset:

    def __init__(self, files):
        self.files = files
        self.fp = open(files[0], 'r')
        self.curr = 0

    def __iter__(self):
        return self

    def __next__(self):
        nextL = self.fp.readline()
        if not nextL:
            self.curr += 1
            if self.curr >= len(self.files): raise StopIteration
            self.fp = open(self.files[self.curr], 'r')
            nextL = self.fp.readline()
            return self.parseBPRI(nextL)
        else:
            return self.parseBPRI(nextL)

    def parseBPRI(self, posts):  # Given a string of posts in BPRI format, return s a list with the label and list of posts
        bpri = posts.split('//POSTDATACOMPILED//')
        bpri[1] = bpri[1].split('/ENDPOST/')

        return bpri


# D = Dataset(['data/compiled-datasets/BPRI-POSTSPLIT/BPRI00.bpri.', 'data/compiled-datasets/BPRI-POSTSPLIT/BPRI01.bpri.'])
# D = iter(D)

# for bpri in D:
    # print(bpri[0], bpri[1][0])
