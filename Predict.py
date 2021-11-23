import torch
import torch.nn as nn
import sys
import dataset
import model

if __name__ == "__main__":
    if (len(sys.argv) > 1) and (sys.argv[1] == '-train'):
        #X = torch.tensor(([2, 9], [1, 5], [3, 6]), dtype=torch.float)  # 3 X 2 tensor
        #y = torch.tensor(([92], [100], [89]), dtype=torch.float)  # 3 X 1 tensor
        #xPredicted = torch.tensor(([4, 8]), dtype=torch.float)  # 1 X 2 tensor
        # scale units
        #X_max, _ = torch.max(X, 0)
        #xPredicted_max, _ = torch.max(xPredicted, 0)

        #X = torch.div(X, X_max)
        #xPredicted = torch.div(xPredicted, xPredicted_max)
        #y = y / 100  # max test score is 100
        #NN = Neural_Network()
        #for i in range(1000):  # trains the NN 1,000 times
            #print("#" + str(i) + " Loss: " + str(torch.mean((y - NN(X)) ** 2).detach().item()))  # mean sum squared loss
            #NN.train(X, y)
        #NN.saveWeights(NN)
        #NN.predict()

        #Get the data to train on and the data to test on
        #scale the data to train on and test on
        #train the network on the data

        pass

    if (len(sys.argv) > 1) and (sys.argv[1] == '-test'):
        pass
