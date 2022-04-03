import numpy as np
import Algorithm as alg
import collections
numHidden = 2
numNodes = [3, 4]
epochs = 500
rate = 0.05
bias = 0
activation = 0

tst = alg.MLP(numHidden, numNodes, epochs, rate, bias, activation)
tst.back_propagation()
tst.test()
# mat = np.zeros((3, 3))
# lst = [1, 2, 3]
# lst = np.array(lst)
#
# mat[lst.index(1)][lst.index(2)] += 1
# print(mat)
