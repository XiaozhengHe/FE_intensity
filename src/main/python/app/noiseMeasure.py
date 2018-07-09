import cv2
import numpy as np


def noise_measuring(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("img", gray)
    cv2.waitKey(0)
    # use GaussianBlur function to blur the image, "gaussian_blur" is the blurred image
    gaussian_blur = cv2.GaussianBlur(gray, (11, 11), 1)
    cv2.imshow("gaussian_blur", gaussian_blur)
    cv2.waitKey(0)
    noise = gray - gaussian_blur + 128
    cv2.imshow("noise", noise)

    variance = np.var(noise)
    print "noise image variance:", variance
    print "noise image mean:", np.mean(noise)
    cv2.waitKey(0)
