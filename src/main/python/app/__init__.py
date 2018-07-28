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
import matplotlib.cm as cm


def main():
    print "12321313"
    i = input(
        "1: video playing; 2: recording and detecting; 3: detecting video; 4: read-time detect; 5: detecting image\n")
    if int(i) == 1:
        videoReceive.videoplaying("../../../test/data/video/001_deliberate_smile_2.mp4")
    elif int(i) == 2:
        if videoReceive.videorecording():
            faceDetect.frontalfacedetectingforvideo("../../../test/data/video/recorded.mov")
        else:
            pass
    elif int(i) == 3:
        faceDetect.frontalfacedetectingforvideo("../../../test/data/video/558_deliberate_smile_1.mp4")
    elif int(i) == 4:
        faceDetect.real_time_detect()
    elif int(i) == 5:
        sub_region = 1
        faces, image = faceDetect.frontalfacedetectingforimg("../../../test/data/img/S132_006_00000008.png")
        noiseMeasure.noise_measuring(image)
        # applyLBP.lbp_for_one_image(faces, image)
        histogram_for_one_image = applyLBPi.lbp_for_one_image(faces, image, sub_region)
    elif int(i) == 6:
        i = 0
        sub_region = 5  # the number of sub-regions, sub-region by sub-region
        p_c = np.zeros(shape=(1, 2))
        print "pc:", p_c
        for folder in ['005', '006']:
            histogram_array = []
            for filename in sorted(os.listdir("../../../test/data/img/%s" % folder))[1:]:
                print "../../../test/data/img/%s/" % folder + filename
                faces, image = faceDetect.frontalfacedetectingforimg("../../../test/data/img/%s/" % folder + filename)
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
        p_c = np.delete(p_c, (0), axis=0)
        print "p_c:", p_c
        # applyPCA.draw_points(p_c, sub_region)
        coordinate_x = p_c[:, 0]
        coordinate_y = p_c[:, 1]
        colors = cm.rainbow(np.linspace(0, 1, len(coordinate_y)))
        for x, y, c in zip(coordinate_x, coordinate_y, colors):
            plt.scatter(x, y, color=c)
        plt.show()
    elif int(i) == 7:
        histogram_array = []
        i = 0
        sub_region = 6  # the number of sub-regions, sub-region by sub-region
        for filename in sorted(os.listdir("../../../test/data/img/005"))[1:]:
            print "../../../test/data/img/005/" + filename
            faces, image = faceDetect.frontalfacedetectingforimg("../../../test/data/img/005/" + filename)
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

