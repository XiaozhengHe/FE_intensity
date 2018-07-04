import cv2


def frontalfacedetectingforimg(img_path):    # return a list of "faces"
    cascade_path = "/Users/hexiaozheng/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)    # create the haar cascade
    image = cv2.imread(img_path)    # read the image
    image_c = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=8,
        flags=cv2.CASCADE_SCALE_IMAGE,
        minSize=(100, 100)
    )    # return a list of rectangles
    print "Found %d faces" % len(faces)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # print faces
    # cv2.imshow("Faces found", image)
    # cv2.waitKey(0)
    return faces, image_c


def frontalfacedetectingforvideo(video_path):    # return a list of faces_s
    cascade_path = "/Users/hexiaozheng/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    list_faces = []
    print "fps:", fps
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=10,
                flags=cv2.CASCADE_SCALE_IMAGE,
                minSize=(100, 100)
            )    # return a list of faces(rectangles)
            fa = []
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                fa = fa + [[x, y, w, h]]
                print faces
            #  fa: faces in one frame, each element is a rectangle(face)
            list_faces = list_faces + [fa]
            #  list_faces: faces in the all frames, each element is a frame
            cv2.imshow("Faces found", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    return list_faces


def real_time_detect():
    cascade_path = "/Users/hexiaozheng/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                flags=cv2.CASCADE_SCALE_IMAGE,
                minSize=(30, 30)
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow("Faces found", frame)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    return
