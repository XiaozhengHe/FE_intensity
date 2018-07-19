import numpy as np
import matplotlib.pyplot as plt
import sklearn.decomposition


def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    arrowprops=dict(arrowstyle='->',
                    linewidth=1,
                    shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)


rng = np.random.RandomState(1)
x = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
plt.scatter(x[:, 0], x[:, 1], alpha=0.2)
pca = sklearn.decomposition.PCA(n_components=1)
# pca.fit(x)
x_pca = pca.fit_transform(x)
print("original shape:   ", x.shape)
print("transformed shape:", x_pca.shape)

X_new = pca.inverse_transform(x_pca)
plt.scatter(x[:, 0], x[:, 1], alpha=0.2)
plt.scatter(X_new[:, 0], X_new[:, 1], alpha=0.8)

for length, vector in zip(pca.explained_variance_, pca.components_):
    v = vector * 3 * np.sqrt(length)
    draw_vector(pca.mean_, pca.mean_ + v)
plt.axis('equal')
print pca.components_
print pca.explained_variance_
print pca.mean_
plt.show()

