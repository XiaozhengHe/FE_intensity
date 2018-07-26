import cv2
import numpy as np
from matplotlib import pyplot as plt


def lbp_histogram(img, number_sub_region, eps=1e-7):
    height, width = img.shape[:2]
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_lbp = np.zeros((height, width, 3), np.uint8)
    region_w = width / number_sub_region   # face sub-region width, equals to face sub-region height
    hist = np.array([])
    if height == width:
        for t in range(0, number_sub_region**2):
            row = t // number_sub_region
            col = t % number_sub_region
            region_img = img_gray[region_w * row: region_w * (row + 1), region_w * col: region_w * (col + 1)]
            region_lbp = img_lbp[region_w * row: region_w * (row + 1), region_w * col: region_w * (col + 1)]
            for i in range(0, region_w):
                for j in range(0, region_w):
                    region_lbp[i, j] = lbp_calculate_pixel(region_img, i, j)

            (region_hist, _) = np.histogram(region_lbp.ravel(), bins=256, range=(0, 2 ** 8))

            # normalize the region histogram for one sub-region of the face
            region_hist = region_hist.astype("float")
            region_hist /= (region_hist.sum() + eps)
            # print "sub-region histogram:", region_hist

            # show the histogram
            plt.style.use("ggplot")
            # fig, ax = plt.subplots()
            plt.title("lbp sub-region histogram")
            #plt.ylabel("percentage")
            #plt.xlabel("bins")
            plt.gray()

            # plt.bar(np.arange(len(region_hist)), region_hist)
            # plt.show()

            # cv2.imshow("lbp implementation image ", region_lbp)
            # cv2.waitKey(0)

            # concatenate the region_hist to hist
            hist = np.concatenate((hist, region_hist), axis=0)

        # plt.bar(np.arange(len(hist)), hist)
        # plt.show()

        # reshape to number = 255 arrays, the histogram for each sub-region
        # print "histogram of all sub-regions:", hist
        # hist = np.reshape(hist, (-1, 256))
        return hist
    else:
        print "The input of this function (lbp_histogram()) is not face, the w and h do not equal."
        return


def lbp_calculate_pixel(img, x, y):
    """

         64 | 128 |   1
        ----------------
         32 |   0 |   2
        ----------------
         16 |   8 |   4

    """
    center = img[x][y]
    val_ar = list()
    val_ar.append(get_pixel(img, center, x - 1, y + 1))  # top_right
    val_ar.append(get_pixel(img, center, x, y + 1))  # right
    val_ar.append(get_pixel(img, center, x + 1, y + 1))  # bottom_right
    val_ar.append(get_pixel(img, center, x + 1, y))  # bottom
    val_ar.append(get_pixel(img, center, x + 1, y - 1))  # bottom_left
    val_ar.append(get_pixel(img, center, x, y - 1))  # left
    val_ar.append(get_pixel(img, center, x - 1, y - 1))  # top_left
    val_ar.append(get_pixel(img, center, x - 1, y))  # top

    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
    val = 0
    for i in range(len(val_ar)):
        val = val + val_ar[i] * power_val[i]
    return val


def get_pixel(img, center, x, y):
    new_value = 0
    try:
        if int(img[x][y]) - int(center) >= 0:
            new_value = 1
    except:
        pass
    return new_value
