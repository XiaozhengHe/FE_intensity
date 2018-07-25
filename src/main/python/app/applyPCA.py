from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def draw_points(histogram_array):
    pca = PCA(n_components=2)
    #pca.fit(histogram_array)
    prin_com = pca.fit_transform(histogram_array)
    #coordinate_x = histogram_array[:, 0]
    #coordinate_y = histogram_array[:, 1]
    coordinate_x = prin_com[:, 0]
    coordinate_y = prin_com[:, 1]
    #plt.scatter(histogram_array[:, 0], histogram_array[:, 1])
    colors = cm.rainbow(np.linspace(0, 1, len(coordinate_y)))
    for x, y, c in zip(coordinate_x, coordinate_y, colors):
        plt.scatter(x, y, color=c)
    print "prin_com:", prin_com
    print "prin_com 0:", prin_com[0]
    print "prin_com 1:", coordinate_y
    print "prin_com len:", len(prin_com)
    print "prin_com[0] len:", len(prin_com[0])
    plt.show()
    print "pca components:", pca.components_
    print "pca variance:", pca.explained_variance_
    #print "principal components:", prin_com.components_
    #print "principal variance:", prin_com.explained_variance_
