import cv2
import face_recognition

wajah=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

vs = cv2.VideoCapture(0)

while True:
    ret, frame = vs.read()

    if frame is None:
        break

    faces = faceCascade.detectMultiScale(frame)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow("Video",frame)
        key = cv2.waitKey(1) & 0xFF

        if key == 27:
            break
video_capture.release()
cv2.destroyAllWindows()