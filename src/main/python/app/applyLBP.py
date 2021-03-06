import cv2
from localbinarypatterns import LocalBinaryPatterns


#    input: a list of faces detected in faceDetect and one image or frame
def lbp_for_one_image(faces, image):
    if len(faces) == 0:
        print "No faces detected."
        return
    elif len(faces) > 1:
        print "Sorry, more than one facial expression is not supported now."
        return
    else:
        x, y, w, h = faces[0]
        img = image[y: y+h, x: x + w]   # face part
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        desc = LocalBinaryPatterns(8, 1)
        desc.describe(gray, 2)

