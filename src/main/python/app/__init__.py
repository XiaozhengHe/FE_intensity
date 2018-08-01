import videoReceive
import faceDetect
import applyLBP
import noiseMeasure
import LBPimplementation
import applyLBPi
import os
import numpy as np
import applyPCA
import applySVM
import matplotlib.pyplot as plt
from sklearn import svm
import cv2


def main():
    print "12321313"
    i = input(
        "1: video playing; 2: recording and detecting; 3: detecting video; 4: read-time detect; 5: detecting image\n")
    if int(i) == 1:
        videoReceive.videoplaying("../../../test/data/video/558_deliberate_smile_1.mp4")
    elif int(i) == 2:
        if videoReceive.videorecording():
            video = cv2.VideoCapture("../../../test/data/video/recorded.mov")
            faceDetect.frontalfacedetectingforvideo(video)
        else:
            pass
    elif int(i) == 3:
        video = cv2.VideoCapture("../../../test/data/video/558_deliberate_smile_1.mp4")
        faceDetect.frontalfacedetectingforvideo(video)
    elif int(i) == 4:
        faceDetect.real_time_detect()
    elif int(i) == 5:
        sub_region = 1
        img = cv2.imread("../../../test/data/img/S132_006_00000008.png")
        faces, image = faceDetect.frontalfacedetectingforimg(img)
        noiseMeasure.noise_measuring(image)
        # applyLBP.lbp_for_one_image(faces, image)
        histogram_for_one_image = applyLBPi.lbp_for_one_image(faces, image, sub_region)
    elif int(i) == 6:
        i = 0
        sub_region = 5  # the number of sub-regions, sub-region by sub-region
        p_c = np.zeros(shape=(1, 2))
        print "pc:", p_c
        #for folder in ['005', '006']:
        for folder in ['S046_005', 'S074_005', 'S125_005', 'S130_013', 'S131_007', 'S132_006', 'S138_005']:
            histogram_array = []
            file_list = sorted(os.listdir("../../../test/data/img/happy_faces/%s" % folder))
            if file_list[0][-4:] != '.png':
                file_list.pop(0)
            for filename in file_list:
                print "../../../test/data/img/happy_faces/%s/" % folder + filename
                img = cv2.imread("../../../test/data/img/happy_faces/%s/" % folder + filename)
                faces, image = faceDetect.frontalfacedetectingforimg(img)
                histogram_for_one_image = applyLBPi.lbp_for_one_image(faces, image, sub_region)
                i = i + 1
                histogram_array = np.concatenate((histogram_array, histogram_for_one_image), axis=0)
                print i
                print filename
                print len(histogram_array)
            histogram_array = np.reshape(histogram_array, (-1, (sub_region ** 2) * 256))
            print histogram_array
            print "len:", len(histogram_array), len(histogram_array[0])
            principal_components = applyPCA.draw_points(histogram_array, sub_region)
            p_c = np.concatenate((p_c, principal_components))
            print "pc:", p_c
        p_c = np.delete(p_c, 0, axis=0)
        print "p_c:", p_c
        # applyPCA.draw_points(p_c, sub_region)
        coordinate_x = p_c[:, 0]
        coordinate_y = p_c[:, 1]
        #colors = cm.rainbow(np.linspace(0, 1, len(coordinate_y)))
        #for x, y, c in zip(coordinate_x, coordinate_y, colors):
        #    plt.scatter(x, y, color=c)
        plt.scatter(coordinate_x, coordinate_y, color='r')
        plt.show()
        applySVM.train_test(p_c)
        '''
        x_training = []
        for i in range(len(p_c[:, 0])):
            x_training = x_training + [[float(p_c[:, 0][i])]]
        print "x_training", x_training

        y_training = p_c[:, 1]
        my_svr = svm.SVR(kernel="linear", C=1e3)
        my_svr.fit(x_training, y_training)
        y_lin = my_svr.predict(x_training)
        plt.plot(x_training, y_lin, color='c', label='Linear model')
        
        plt.show()
        '''
    elif int(i) == 7:
        histogram_array = []
        i = 0
        sub_region = 6  # the number of sub-regions, sub-region by sub-region
        for filename in sorted(os.listdir("../../../test/data/img/005"))[1:]:
            print "../../../test/data/img/005/" + filename
            img = cv2.imread("../../../test/data/img/005/" + filename)
            faces, image = faceDetect.frontalfacedetectingforimg(img)
            histogram_for_one_image = applyLBPi.lbp_for_one_image(faces, image, sub_region)
            i = i + 1
            histogram_array = np.concatenate((histogram_array, histogram_for_one_image), axis=0)
            print i
            print filename
            print len(histogram_array)
        histogram_array = np.reshape(histogram_array, (-1, (sub_region ** 2) * 256))
        print histogram_array
        print "len:", len(histogram_array), len(histogram_array[0])
        principal_components = applyPCA.draw_points(histogram_array, sub_region)
        applySVM.train_test(principal_components)


if __name__ == '__main__':
    main()

