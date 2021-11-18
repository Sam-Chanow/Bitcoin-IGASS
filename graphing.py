# SAM CHANOW
# A collection of helper functions for graphing dataset and model information

from sklearn.model_selection import learning_curve
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import dataset
from dataset import Dataset
from itertools import tee


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

def graph_BVBPRI_UP_Postcount_Correlation():
    D = Dataset(['data/compiled-datasets/BVBPRI/BVBPRI' + str(x) + '.pt' for x in range(800, 967)], tensor_data=True)
    D = iter(D)

    files = [x for x in range(800, 967)]
    sizes = []
    direction = []
    count = 0  # for debug

    for x in D:
        print("DAY", count)
        sizes.append(len(x[1]))
        direction.append(len(x[1]) * (2/3) if x[0] == 'UP ' else 0)
        count += 1

    print(direction)

    fig, ax = plt.subplots()
    ax.plot(files, sizes)
    ax.bar(files, direction)

    ax.legend(["Posts per day", "If the price of Bitcoin rose the following day"])

    ax.set(xlabel='Day (# since OCT 25 2018)', ylabel='# of posts from day',
           title='Post Frequency and Bitcoin Price Rise and Fall')
    ax.grid()

    fig.savefig("images/postfrequencytoUPDOWN.png")
    plt.show()

def priceUP_DOWN():
    D = Dataset(['data/compiled-datasets/BVBPRI/BVBPRI' + str(x) + '.pt' for x in range(800, 967)], tensor_data=True)
    D = iter(D)

    files = [x for x in range(800, 967)]

    updays = []
    upnums = []
    downdays = []
    downnums = []
    count = 800

    for x in D:
        print("DAY", count)

        if x[0] == 'UP ':
            updays.append(count)
            upnums.append(len(x[1]))

        if x[0] == 'DOWN ':
            downdays.append(count)
            downnums.append(len(x[1]))

        #sizes.append(len(x[1]))
        #direction.append(len(x[1]) * (2/3) if x[0] == 'UP ' else 0)
        count += 1

    fig, ax = plt.subplots()
    ax.scatter(updays, upnums, c='green')
    ax.scatter(downdays, downnums, c='red')

    ax.legend(["Post# if Price Increase", "Post# if Price Decrease"])

    ax.set(xlabel='Day (# since OCT 25 2018)', ylabel='# of posts from day',
           title='Post Frequency and Bitcoin Price Rise and Fall')
    ax.grid()

    fig.savefig("images/dualGraphUpDOWN.png")
    plt.show()


def bar_test():
    x = [x for x in range(10)]
    y = [x for x in range(10)]

    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.grid()
    plt.show()

priceUP_DOWN()
