import sklearn.svm
import cv2
import faceDetect
import applyLBPi
import applyPCA
import numpy as np


def happy_level(cap, sub_region, my_svm, y_lin):
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # FPS of the video
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # total count of the frame of the video
    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if (i % 10 == 0) and (i != 0):
                faces, image = faceDetect.frontalfacedetectingforimg(frame)
                hist = applyLBPi.lbp_for_one_image(faces, image, sub_region)
                hist = np.reshape(hist, (-1, (sub_region ** 2) * 256))
                principal_component = applyPCA.draw_points(hist, sub_region)

                x_testing = []
                for i in range(len(principal_component[:, 0])):
                    x_testing = x_testing + [[float(principal_component[:, 0][i])]]
                print "x_testing", x_testing

                y_value = my_svm.predict(x_testing)

                min_value = float(min(y_lin))
                max_value = float(max(y_lin))

                if float(y_value[0]) < min_value:
                    print "happy level: 1"
                elif float(y_value[0]) > max_value:
                    print "happy level: 10"
                else:
                    perc = (y_value - min_value) / (max_value - min_value) * 100
                    print "happy level: %s" % str(perc) + " %"
            cv2.namedWindow("Video Playing", cv2.WINDOW_NORMAL)
            frameS = cv2.resize(frame, (960, 540))
            cv2.imshow("Video Playing", frameS)
            i = i + 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    pass
