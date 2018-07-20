from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def draw_points(histogram_array):
    pca = PCA(n_components=2)
    pca.fit(histogram_array)
    plt.scatter(histogram_array[:, 0], histogram_array[:, 1])
    plt.show()
    print "pca components:", pca.components_
    print "pca variance:", pca.explained_variance_
