import videoReceive
import faceDetect

if __name__ == '__main__':
    print "12321313"
    i = input("1: video playing; 2: recording and detecting; 3: detecting video; 4: read-time detect; 5: detecting image\n")
    if int(i) == 1:
        videoReceive.videoplaying("../../../test/data/video/video.mov")
    elif int(i) == 2:
        if videoReceive.videorecording():
            faceDetect.frontalfacedetectingforvideo("../../../test/data/video/recorded.mov")
        else:
            pass
    elif int(i) == 3:
        faceDetect.frontalfacedetectingforvideo("../../../test/data/video/video.mov")
    elif int(i) == 4:
        faceDetect.real_time_detect()
    else:
        faceDetect.frontalfacedetectingforimg("../../../test/data/img/abba.png")
else:
    print "please run __init__.py"

