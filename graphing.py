# SAM CHANOW
# A collection of helper functions for graphing dataset and model information

from sklearn.model_selection import learning_curve
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import dataset
from dataset import Dataset

def graph_BVBPRI_size():
    D = Dataset(['data/compiled-datasets/BVBPRI/BVBPRI' + str(x) + '.pt' for x in range(967)], tensor_data=True)
    D = iter(D)

    files = [x for x in range(967)]
    sizes = [len(x[1]) for x in D]

    fig, ax = plt.subplots()
    ax.plot(files, sizes)
    ax.set(xlabel='Day (# since OCT 25 2018)', ylabel='# of posts from day',
           title='Post Frequency vs Time in BVBPRI Dataset')
    ax.grid()

    fig.savefig("images/datafrequency.png")
    plt.show()

