from skimage import feature
import numpy as np
from matplotlib import pyplot as plt


class LocalBinaryPatterns:
    def __init__(self, numpoints, radius):
        # store the number of points and radius
        self.numPoints = numpoints
        self.radius = radius

    def describe(self, gray_image, eps=1e-7):
        # compute the Local Binary Pattern representation
        # of the image, and then use the LBP representation
        # to build the histogram of patterns
        lbp = feature.local_binary_pattern(gray_image, self.numPoints, self.radius, method="uniform")
        # cv2.imshow("LBP", lbp.astype(np.uint8)) # show method="default" lbp image, but cannot show method="uniform"
        (hist, _) = np.histogram(lbp.ravel(),
                                 bins=np.arange(0, self.numPoints + 3),
                                 range=(0, self.numPoints + 2))

        print "hist:", hist

        # normalize the histogram
        hist = hist.astype("float")
        hist /= (hist.sum() + eps)

        # return the histogram of Local Binary Patterns
        print "hist after normalizing", hist
        # showing the lbp image using plt
        plt.imshow(lbp, cmap="gray")
        plt.show()
        return hist
