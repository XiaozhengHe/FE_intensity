import cv2
import numpy as np
import xlsxwriter


def noise_measuring(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("img", gray)
    cv2.waitKey(0)
    # use GaussianBlur function to blur the image, "gaussian_blur" is the blurred image
    gaussian_blur = cv2.GaussianBlur(gray, (5, 5), 5)
    cv2.imshow("gaussian_blur", gaussian_blur)
    cv2.waitKey(0)
    noise = gray - gaussian_blur + 128
    cv2.imshow("noise", noise)
    cv2.imwrite("../../../test/data/img/noise.jpg", noise)

    print "noise image:", noise

    workbook = xlsxwriter.Workbook("../../../test/data/excel/noise_image.xlsx")
    worksheet = workbook.add_worksheet()
    for row, data in enumerate(noise):
        worksheet.write_row(row, 0, data)

    variance = np.var(noise)
    print noise[0][0]
    print "noise image variance:", variance
    print "noise image standard deviation:", np.std(noise, ddof=1)
    print "noise image mean:", np.mean(noise)
    cv2.waitKey(0)
