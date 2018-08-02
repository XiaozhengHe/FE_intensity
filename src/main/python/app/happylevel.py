import sklearn.svm
import cv2
import faceDetect
import applyLBPi
import applyPCA
import numpy as np


def happy_pca(cap_path, sub_region):
    cap = cv2.VideoCapture(cap_path)
    i = 0
    histogram_array = []
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if (i % 10 == 0) and (i != 0):
                print "Now applying the LBP algorithm in this video in frame:", str(i)
                faces, image = faceDetect.frontalfacedetectingforimg(frame)
                # one frame histogram
                hist = applyLBPi.lbp_for_one_image(faces, image, sub_region)
                # hist = np.reshape(hist, (-1, (sub_region ** 2) * 256))
                # select 1 frame from each 10, and compose "histogram_array"
                histogram_array = np.concatenate((histogram_array, hist), axis=0)
            i = i + 1
        else:
            break
    cap.release()
    # cv2.destroyAllWindows()
    histogram_array = np.reshape(histogram_array, (-1, (sub_region ** 2) * 256))
    print "Now applying PCA in these frames selected..."
    principal_component = applyPCA.draw_points(histogram_array, sub_region)
    return principal_component


def happy_level(cap_path, my_svm, y_lin, principal_component):
    cap = cv2.VideoCapture(cap_path)
    i = 0
    t = 0
    x_testing = []
    for c_i in range(len(principal_component[:, 0])):
        x_testing = x_testing + [[float(principal_component[:, 0][c_i])]]
    # print "x_testing", x_testing
    y_result = my_svm.predict(x_testing)
    min_y = min(y_lin)
    max_y = max(y_lin)
    print "Below showing the happy facial expression indices:"
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if (i % 10 == 0) and (i != 0):
                if y_result[t] <= min_y:
                    print "happy_level: 10%"
                elif y_result[t] >= max_y:
                    print "happy_level: 95%"
                else:
                    perc = (y_result[t] - min_y) / (max_y - min_y) * 100
                    print "happy_level: %s" % str(perc) + "%"
                t = t + 1
            cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
            frame_resize = cv2.resize(frame, (960, 540))
            cv2.imshow("Video", frame_resize)
            i = i + 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
