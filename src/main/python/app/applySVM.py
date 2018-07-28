from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np


def train_test(principal_component):
    x_training = principal_component
    #x_training = []
    #for i in range(len(principal_component[:, 0])):
    #    x_training = x_training + [[float(principal_component[:, 0][i])]]
    print "x_training", x_training
    len_p = len(principal_component)

    y_training = principal_component[:, 1]

    # y_training = np.arange(0, 1, 1.0/len_p)

    #x_test = x_training[0]
    #y_res = y_training[0]
    my_svr = svm.SVR(kernel="linear")
    my_svr.fit(x_training, y_training)
    #p = my_svr.predict([x_test])
    #print "x_training[0]:", x_test
    #print "y_res", y_res
    #print "predict:", p
    plt.plot(x_training, my_svr.predict(x_training), label='True data')

    plt.show()
