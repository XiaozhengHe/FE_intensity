import cv2
import os
import numpy


def videoplaying():
    video_path = "../../../test/data/video/video.mov"
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1000/int(fps)) & 0xFF == ord('q'):
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
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    video_path = "../../../test/data/video/recorded.mov"
    if os.path.exists(video_path):
        os.remove(video_path)
    out = cv2.VideoWriter(video_path, fourcc, fps, (int(w), int(h)))
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow("Frame", frame)
        if cv2.waitKey(1000/int(fps)) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
