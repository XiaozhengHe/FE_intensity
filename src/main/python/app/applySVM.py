from sklearn import svm
import matplotlib.pyplot as plt


def train_test(principal_component):
    x_training = []
    for i in range(len(principal_component[:, 0])):
        x_training = x_training + [[float(principal_component[:, 0][i])]]
    print "x_training", x_training

    y_training = principal_component[:, 1]
    my_svr = svm.SVR(kernel="linear", C=1e3)
    my_svr.fit(x_training, y_training)
    y_lin = my_svr.predict(x_training)
    plt.plot(x_training, y_lin, color='c', label='Linear model')

    plt.show()
