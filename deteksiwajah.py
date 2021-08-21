import numpy as np 
import cv2 

wajah=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('2.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

deteksi_wajah=wajah.detectMultiScale(img_gray,1.1,5)
font=cv2.FONT_HERSHEY_SIMPLEX
jumlah=0

for (x,y,w,h) in deteksi_wajah:
	jumlah = jumlah +1
	#cv2.putText(img,"Wajah",(x,y-10),font,0.75,(0,0,255),2,cv.LINE_AA)
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray=img_gray[y:y+h,x:x+w]
	roi_color=img[y:y+h,x:x+w]

cv2.putText(img,"Jumlah wajah ada : "+str(jumlah)+" buah",(10,30),font,1,(0,0,0),2,cv2.LINE_AA)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()