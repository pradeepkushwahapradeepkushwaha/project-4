import cv2

url='http://192.168.43.1:8080/video'

cap= cv2.VideoCapture(url)





while(True):

    seccess,img=cap.read()
    if img is not None :
        
     cv2.imshow('img',img)

    q=cv2.waitKey(1)
    if q==ord("q"):
       break
cv2.destroyAllWindows()    
    