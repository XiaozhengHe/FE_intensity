import sklearn.svm
import cv2


def happy_level(svm, cap):
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # FPS of the video
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # total count of the frame of the video
    
    pass
