import videoReceive
import faceDetect
import applyLBP
import noiseMeasure
import LBPimplementation
import applyLBPi
import happylevel
import os
import numpy as np
import applyPCA
import applySVM
import matplotlib.pyplot as plt
from sklearn import svm
import cv2


def main():
    cap_path = "../../../test/data/video/017_deliberate_smile_1.mp4"
    recorded_path = "../../../test/data/video/recorded.mov"
    image_path = "../../../test/data/img/S132_006_00000008.png"
    i = input(
        "1: Detecting faces from an image;\n"
        "2: Video playing;\n"
        "3: Recording and detecting faces;\n"
        "4: Detecting faces from a video;\n"
        "5: Real-time detecting faces;\n"
        "6: Showing happiness indices.\n")
    if int(i) == 1:
        sub_region = 1
        img = cv2.imread(image_path)
        faces, image = faceDetect.frontalfacedetectingforimg(img)
        noiseMeasure.noise_measuring(image)
        # applyLBP.lbp_for_one_image(faces, image)
        histogram_for_one_image = applyLBPi.lbp_for_one_image(faces, image, sub_region)
    elif int(i) == 2:
        videoReceive.videoplaying(cap_path)
    elif int(i) == 3:
        if videoReceive.videorecording():
            video = cv2.VideoCapture(recorded_path)
            faceDetect.frontalfacedetectingforvideo(video)
        else:
            pass
    elif int(i) == 4:
        video = cv2.VideoCapture(cap_path)
        length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # total count of the frame of the video
        print "frame number:", length
        faceDetect.frontalfacedetectingforvideo(video)
    elif int(i) == 5:
        faceDetect.real_time_detect()
    elif int(i) == 6:
        i = 0
        sub_region = 5  # the number of sub-regions, sub-region by sub-region
        # cap_path = "../../../test/data/video/010_deliberate_smile_3.mp4"  # the path of the video detecting
        p_c = np.zeros(shape=(1, 2))
        for folder in ['S046_005', 'S074_005', 'S130_013', 'S132_006']:
            histogram_array = []
            file_list = sorted(os.listdir("../../../test/data/img/happy_faces/%s" % folder))
            if file_list[0][-4:] != '.png':
                file_list.pop(0)
            for filename in file_list:
                # print "../../../test/data/img/happy_faces/%s/" % folder + filename
                img = cv2.imread("../../../test/data/img/happy_faces/%s/" % folder + filename)
                faces, image = faceDetect.frontalfacedetectingforimg(img)
                histogram_for_one_image = applyLBPi.lbp_for_one_image(faces, image, sub_region)
                i = i + 1
                histogram_array = np.concatenate((histogram_array, histogram_for_one_image), axis=0)
                print "Detecting face and apply LBP in image:", filename
            histogram_array = np.reshape(histogram_array, (-1, (sub_region ** 2) * 256))
            #print histogram_array
            #print "len:", len(histogram_array), len(histogram_array[0])
            principal_components = applyPCA.draw_points(histogram_array, sub_region)
            p_c = np.concatenate((p_c, principal_components))
            print "Apply PCA in folder:", folder
            #print "pc:", p_c
        p_c = np.delete(p_c, 0, axis=0)
        #print "p_c:", p_c
        # applyPCA.draw_points(p_c, sub_region)
        # coordinate_x = p_c[:, 0]
        # coordinate_y = p_c[:, 1]
        # colors = cm.rainbow(np.linspace(0, 1, len(coordinate_y)))
        # for x, y, c in zip(coordinate_x, coordinate_y, colors):
        #     plt.scatter(x, y, color=c)
        # plt.scatter(coordinate_x, coordinate_y, color='r')
        # plt.show()
        my_svm, y_lin = applySVM.train_test(p_c)
        # cap = cv2.VideoCapture(cap_path)
        prin_component = happylevel.happy_pca(cap_path, sub_region)
        happylevel.happy_level(cap_path, my_svm, y_lin, prin_component)
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


if __name__ == '__main__':
    main()

