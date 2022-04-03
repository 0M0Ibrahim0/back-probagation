import numpy as np


class Helper:

    def load_data(self):
        classes = {'Iris-setosa': [1, 0, 0], 'Iris-versicolor': [0, 1, 0], 'Iris-virginica': [0, 0, 1]}
        x = []
        labels = []
        with open('data.txt') as f:
            lines = map(lambda l: l.rstrip().split(','), f.readlines())
            for line in lines:
                if line[0] == 'X1':
                    continue
                x.append([float(i) for i in line[:4]])
                labels.append(classes[line[4]])

        x = np.array(x)
        labels = np.array(labels)
        return x, labels
#################################################
    def activation(self, A, type, deriv = False):
        if type == 0:
            return self.sigmoid(A,deriv)
        else:
            return self.hyperbolic_tangent(A, deriv)

    def sigmoid(self, A, deriv=False):
        if deriv == True:  # derivative of sigmoid
            # A = np.multiply(A, np.subtract(1, A))
            for i in range(len(A)):
                A[i] = A[i] * (1 - A[i])
        else:
            #A = np.division(1, (np.add(1, np.exp(-A))))
            for i in range(len(A)):
                A[i] = 1 / (1 + np.exp(-A[i]))
        return A

    def hyperbolic_tangent (self, A, deriv = False):

        if deriv:  # derivative of Hyperbolic Tangent
            for i in range(len(A)):
                A[i] = ( 1 - (np.tanh(A[i]) ** 2) )
        else:
            for i in range(len(A)):
                A[i] = np.tanh(A[i])
        return A

    pass
