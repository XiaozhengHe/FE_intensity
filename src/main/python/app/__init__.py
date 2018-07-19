import videoReceive
import faceDetect
import applyLBP
import noiseMeasure
import LBPimplementation
import applyLBPi


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
        faces, image = faceDetect.frontalfacedetectingforimg("../../../test/data/img/S132_006_00000008.png")
        noiseMeasure.noise_measuring(image)
        # applyLBP.lbp_for_one_image(faces, image)
        applyLBPi.lbp_for_one_image(faces, image)


if __name__ == '__main__':
    main()

