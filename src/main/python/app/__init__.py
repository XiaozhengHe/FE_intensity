import videoReceive
import faceDetect

if __name__ == '__main__':
    print "12321313"
    i = input("shuru")
    if int(i) == 1:
        videoReceive.videoplaying()
    elif int(1) ==2:
        videoReceive.videorecording()
        faceDetect.frontalfacedetectingforvideo()
    else:
        faceDetect.frontalfacedetectingforvideo()
else:
    print "please run __init__.py"

