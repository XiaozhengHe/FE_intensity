from skimage import feature
import numpy as np
from matplotlib import pyplot as plt
import cv2


class LocalBinaryPatterns:
    def __init__(self, numpoints, radius):
        # store the number of points and radius
        self.numPoints = numpoints
        self.radius = radius

    def describe(self, gray_image, number_subregion, eps=1e-7):
        # compute the Local Binary Pattern representation
        # of the image, and then use the LBP representation
        # to build the histogram of patterns
        height, width = gray_image.shape[:2]
        region_w = width/number_subregion
        # print "h+w:", height, width
        hist = np.array([])
        if height == width:
            for i in range(number_subregion**2):
                row = i // number_subregion
                col = i % number_subregion
                region_img = gray_image[region_w*row: region_w*(row+1), region_w*col: region_w*(col+1)]
                region_lbp = feature.local_binary_pattern(region_img, self.numPoints, self.radius, method="default")
                cv2.imshow("LBP", region_lbp.astype(np.uint8)) # show method="default" lbp image, but cannot show method="uniform"
                cv2.waitKey(0)
                (region_hist, _) = np.histogram(region_lbp.ravel(),
                                                bins=np.arange(0, self.numPoints + 3),
                                                range=(0, self.numPoints+2))

                # normalize the region histogram
                region_hist = region_hist.astype("float")
                region_hist /= (region_hist.sum() + eps)
                print "single region histogram:", region_hist


                # concatenate the region_hist to his
                hist = np.concatenate((hist, region_hist), axis=0)

            hist = np.reshape(hist, (-1, self.numPoints + 2))
            print "histogram of all sub-region:", hist
            return hist
        else:
            pass
