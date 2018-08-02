import LBPimplementation


#    input: a list of faces detected in faceDetect and one image or frame
def lbp_for_one_image(faces, image, sub_region):
    if len(faces) == 0:
        print "No faces detected."
        return
    elif len(faces) > 1:
        print "Detect %d faces in one frame, only one face in one frame is supported." % len(faces)
        x, y, w, h = faces[0]
        face = image[y: y + h, x: x + w]  # face part
        return LBPimplementation.lbp_histogram(face, sub_region)
    else:
        x, y, w, h = faces[0]
        face = image[y: y+h, x: x + w]   # face part
        return LBPimplementation.lbp_histogram(face, sub_region)

