import numpy as np
import random
from sklearn.model_selection import train_test_split
from Task1.Helper import *


class MLP:

    def __init__(self, numHidden, numNodes, epochs, rate, bias, activation):
        self.numInput, self.numHidden, self.numOutput, self.numNodes = 4, numHidden, 3, numNodes
        self.epochs, self.rate, self.bias, self.activation = epochs, rate, bias, activation
        self.train_x, self.train_y, self.test_x, self.test_y = self.split()
        self.weights, self.bias_weight = self.initializeWeights()
        self.helper = Helper()

    def split(self):
        features, labels = Helper.load_data(0)

        # split data into train , test
        train_x, test_x , train_y, test_y = train_test_split(features, labels, test_size=0.40,shuffle=True)

        # shuffle trained data
        temp = list(zip(train_x, train_y))
        random.shuffle(temp)
        train_x, train_y = zip(*temp)
        train_x, train_y = np.asarray(train_x), np.asarray(train_y)

        return train_x, train_y, test_x, test_y

    ############# initialize weights with small value #################
    def initializeWeights(self):

        self.numNodes.insert(0, self.numInput)
        self.numNodes.append(self.numOutput)

        weight = []
        for i in range(len(self.numNodes) - 1):
            weight.append(np.random.uniform(low=-1, high=1, size=(self.numNodes[i], self.numNodes[i+1])))

        wt_bias = []
        for i in range(len(self.numNodes) - 1):
            wt_bias.append(np.random.uniform(low=-1, high=1, size=(self.numNodes[i+1], 1)))

        return np.array(weight), np.array(wt_bias)


    def back_propagation(self):
        for o_o in range(self.epochs):
            for i in range(len(self.train_x)):
                ############## forward ###################
                net = []
                net.append(self.train_x[i])
                net[0] = np.reshape(net[0], (1, -1))
                for j in range(1, len(self.numNodes)):
                    x = np.array(net[j-1])
                    x = np.reshape(x, (1, -1))
                    w = self.weights[j-1]
                    b = self.bias_weight[j-1] * self.bias
                    y = np.dot(x, w) + b.T
                    y = self.helper.activation(y, self.activation)
                    net.append(y)

                ############### backward ####################
                idx_net = len(net)-1
                segma = []
                z = net[idx_net]
                error = (self.train_y[i] - z) * self.helper.activation(z, self.activation, True)
                segma.append(error)
                idx_net -= 1
                idx_wt = len(self.weights)-1

                for j in range(idx_net, 0,-1):
                    last_segma = segma[len(segma)-1]
                    tmp = 0
                    if self.activation == 0:
                        tmp = net[j] * (1 - net[j])
                    else:
                        tmp = (1 - (np.tanh(net[j]) ** 2))
                    error = tmp * np.dot(last_segma, self.weights[idx_wt].T)
                    idx_wt -= 1
                    segma.append(error)

                ################ update weights ##################
                segma.reverse()
                for j in range(len(segma)):
                    self.weights[j] += self.rate * np.dot(net[j].T, segma[j])
                    self.bias_weight[j] += self.rate * segma[j].T


    def test(self):
        cnt = 0
        matrix = np.zeros((3, 3))
        for i in range(len(self.test_x)):
            ############## forward ###################
            net = []
            net.append(self.test_x[i])
            net[0] = np.reshape(net[0], (1, -1))
            for j in range(1, len(self.numNodes)):
                x = np.array(net[j - 1])
                x = np.reshape(x, (1, -1))
                w = self.weights[j - 1]
                b = self.bias_weight[j - 1] * self.bias
                y = np.dot(x, w) + b.T
                y = self.helper.activation(y, self.activation)
                net.append(y)

            out = self.convert(net[len(net)-1])
            predicted = self.test_y[i]

            p = self.get_index_of_one(predicted)
            o = self.get_index_of_one(out)
            matrix[p][o] += 1
            for o in range(len(out)):
                if out[o] != predicted[o]:
                    cnt += 1
                    break
        return self.accuracy(cnt),matrix

    def convert(self, a):
        a = a[0]
        a[a >= max(a)] = 1
        a[a < max(a)] = 0

        return a

    def accuracy(self, a):
        return ((len(self.test_y) - a) / len(self.test_y)) * 100

    def get_index_of_one(self, a):
        for i in range(len(a)):
            if a[i] == 1:
                return i
