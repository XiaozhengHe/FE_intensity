from skimage import feature
import numpy as np
from matplotlib import pyplot as plt
import cv2


class LocalBinaryPatterns:
    def __init__(self, numpoints, radius):
        # store the number of points and radius
        self.numPoints = numpoints
        self.radius = radius

    def describe(self, image, eps=1e-7):
        # compute the Local Binary Pattern representation
        # of the image, and then use the LBP representation
        # to build the histogram of patterns
        lbp = feature.local_binary_pattern(image, self.numPoints,
                                           self.radius, method="uniform")
        cv2.imshow("lbp", lbp)
        cv2.waitKey(0)
        (hist, _) = np.histogram(lbp.ravel(),
                                 bins=np.arange(0, self.numPoints + 3),
                                 range=(0, self.numPoints + 2))

        print "hist:", hist

        # normalize the histogram
        hist = hist.astype("float")
        hist /= (hist.sum() + eps)

        # return the histogram of Local Binary Patterns
        print "hist after normalizing", hist
        plt.imshow(lbp)
        plt.show()
        return hist
