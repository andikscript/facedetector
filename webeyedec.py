"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""
import cv2


def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        wajah=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
        ret_val, img = cam.read()
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        deteksi_wajah=wajah.detectMultiScale(img_gray,1.1,5)
        font=cv2.FONT_HERSHEY_SIMPLEX
        jumlah=0

        for (x,y,w,h) in deteksi_wajah:
            jumlah = jumlah +1
            #cv2.putText(img,"Wajah",(x,y-10),font,0.75,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
            roi_gray=img_gray[y:y+h,x:x+w]
            roi_color=img[y:y+h,x:x+w]


        cv2.putText(img,"Jumlah Orang = "+str(jumlah),(10,40),font,1,(0,0,0),1,cv2.LINE_AA)
        #untuk membuat warna hitam putih di webcam, kalo mau warna 
        #tinggal ubah gray yang di cv2.imshow dibawah ini dengan img
        gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #cv2.putText(img,"Jumlah wajah ada : "+str(jumlah)+" buah")
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('Deteksi Wajah', gray)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()

