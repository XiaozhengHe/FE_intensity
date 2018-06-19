import cv2
import numpy


def videoplaying():
    cap = cv2.VideoCapture("../../../test/data/video.mov")
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


def videorecording():
    cap = cv2.VideoCapture(0)
    fps = cap.get(cv2.CAP_PROP_FPS)
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("../../../../../../123.avi", fourcc, fps, (int(w), int(h)))
    while 1:
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


