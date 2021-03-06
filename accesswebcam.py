"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""
import cv2


def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    gambar = 1
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27:
            fileN=str(gambar)+'.png'# membuat string nama image yang disimpan
            cv2.imwrite(fileN,img)# simpan image di folder yang aktif sekarang
            print(gambar)# menampilkan nama image yang telah tersimpan di command prompt(CMD) / console terminal
            gambarr = gambar+1 # increase variable penamaan image agar penyimpanan selanjutnya tidak menimpa file yang lama 
            break  # esc to quit
    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()

