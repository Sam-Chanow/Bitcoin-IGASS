import torch
import sys
from tqdm import tqdm
from dataset import Dataset
import numpy as np
import tensorflow as tf

#adding the model folder path
sys.path.append('model/')
sys.path.append('tensorflow_model/')

import model
import tf_model

if __name__ == "__main__":
    if (len(sys.argv) > 1) and (sys.argv[1] == '-train'):
        #Build the dataset from BVBPRI data
        D = Dataset(['data/compiled-datasets/BVBPRI/BVBPRI' + str(x) + '.pt' for x in range(0, 967)],tensor_data=True) #967
        D = iter(D)

        X = []
        count = 0

        for x in tqdm(D):
            x[1] = model.average_tensors(x[1]).tolist()
            #print(x[1])
            x[0] = model.build_labels(x[0])
            #print(x)
            X.append([x[0], x[1]])
            #print(L)
            #print(len(L[0][1]))
            #exit(0)
            count += 1
            #print("Tensor", count, "averaged.")
            if count > 1000: break;


        #print(X[0])
        Y = [t[0] for t in X]
        X = [t[1] for t in X]

        #print("RAW Y:", Y)

        tfm = tf_model.TFModel()
        data = tfm.preprocess(X, Y)

        print("DATA:", [x for x, y in data])

        #exit(0)


        #print("DATA:", y_labels)
        #exit(0)
        train_data, validation_data, test_data = tf_model.get_dataset_partitions(data, 967)
        print("VAL DATA:", [x for x, y in validation_data])
        print("train take", [x for x, y in train_data])
        #for i in iter(data):
            #print(i)

        #num = 300
        #D_eval = Dataset(['data/compiled-datasets/BVBPRI/BVBPRI' + str(x) + '.pt' for x in range(900, 966)], tensor_data=True)
        #D_eval = iter(D_eval)
        #X_eval = []
        #for x in D_eval:
            #x[1] = model.average_tensors(x[1]).tolist()
            #x[0] = model.build_labels(x[0])
            # print(x)
            #X_eval.append([x[0], x[1]])

       # Y_eval = [t[0] for t in X_eval]
        #X_eval = [t[1] for t in X_eval]

        #data_eval = tfm.preprocess(X_eval, Y_eval)

        #for evalu, gold in zip(tfm.evaluate(data_eval), Y_eval):
           # print("OUT:", evalu)
            #print("GOLD:", gold)

        tfm.train(train_data, validation_data)
        y_labels = np.concatenate([y for x, y in test_data], axis=0)
        x_data = np.concatenate([x for x, y in test_data], axis=0)
        score = tfm.evaluate(x_data, y_labels)
        print(f'Test loss: {score[0]} / Test accuracy: {score[1]}')


        #X = torch.tensor(([2, 9], [1, 5], [3, 6]), dtype=torch.float)  # 3 X 2 tensor
        #Y = [torch.FloatTensor(l[0]) for l in X]
        #X = [l[1] for l in X]

        #X = torch.stack(X)
        #Y = torch.stack(Y)
        #print(X.size())



        #print(Y, X)
        #y = torch.tensor(([92], [100], [89]), dtype=torch.float)  # 3 X 1 tensor
        #xPredicted = torch.tensor(([4, 8]), dtype=torch.float)  # 1 X 2 tensor
        # scale units
        #X_max, _ = torch.max(X, 0)
        #xPredicted_max, _ = torch.max(xPredicted, 0)

        #X = torch.div(X, X_max)
        #xPredicted = torch.div(xPredicted, xPredicted_max)
        #y = y / 100  # max test score is 100
        #NN = Net.NNetwork()
        #Loss = []
        #for i in range(1000):  # trains the NN 1,000 times
           # l = str(torch.mean((Y - NN(X)) ** 2).detach().item())
            #print("#" + str(i) + " Loss: " + l)  # mean sum squared loss
           # Loss.append(l)
           # NN.train(X, Y)
        #NN.saveWeights(NN)
        #torch.save(Loss, "model/loss.pt")
        #NN.predict()

        #Get the data to train on and the data to test on
        #scale the data to train on and test on
        #train the network on the data

        pass

    if (len(sys.argv) > 1) and (sys.argv[1] == '-test'):
        pass
        #None of this works yet, needs to be replaced for compatability with tensorflow model
        M = torch.load("NN") #model/loss.pt")
        num = 300
        D = Dataset(['data/compiled-datasets/BVBPRI/BVBPRI' + str(num) + '.pt'], tensor_data=True)
        D = iter(D)
        X = []
        for x in D:
            x[1] = model.average_tensors(x[1])
            x[0] = model.build_labels(x[0])
            # print(x)
            X.append([x[0], x[1]])

        Y = [torch.FloatTensor(l[0]) for l in X]
        X = [l[1] for l in X]

        X = torch.stack(X)
        Y = torch.stack(Y)

        print(X.size())
        output = M(X[0])
        print("OUTPUT:", output, "LABEL:", Y[0])
