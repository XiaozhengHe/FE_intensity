from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def draw_points(histogram_array, sub_region):
    pca = PCA(n_components=2)
    # pca.fit_transform(histogram_array)
    pca.fit(histogram_array)
    print "pca components:", pca.components_
    print "fit pca variance ratio:", pca.explained_variance_ratio_
    prin_com = pca.transform(histogram_array)
    # coordinate_x = histogram_array[:, 0]
    # coordinate_y = histogram_array[:, 1]
    coordinate_x = prin_com[:, 0]
    coordinate_y = prin_com[:, 1]
    colors = cm.rainbow(np.linspace(0, 1, len(coordinate_y)))
    for x, y, c in zip(coordinate_x, coordinate_y, colors):
        plt.scatter(x, y, color=c)
    #plt.scatter(coordinate_x, coordinate_y)
    print "prin_com:", prin_com
    print "prin_com len:", len(prin_com)
    print "prin_com[0] len:", len(prin_com[0])
    plt.title("facial expression points with " + str(sub_region ** 2) + " sub-region")
    plt.xlabel("principal component")
    plt.ylabel("principal component values")
    plt.show()
    return prin_com
