import cv2
import os


def videoplaying(video_path):
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
    try:
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
    except:
        print "Video recording fails."
        return False
    else:
        return True
