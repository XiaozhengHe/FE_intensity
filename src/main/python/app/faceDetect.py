import cv2


def frontalfacedetecting():
    p = "/Users/hexiaozheng/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(p)    # create the haar cascade
    image = cv2.imread("../../../test/data/abba.png")    # read the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        flags=cv2.CASCADE_SCALE_IMAGE,
        minSize=(30, 30)
    )    # return a list of rectangles
    print "Found {0} faces".format(len(faces))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h),(0, 255, 0), 2)
    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
