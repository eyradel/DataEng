import cv2
from cvzone.FaceDetectionModule import FaceDetector
detector = FaceDetector()
cap =cv2.VideoCapture(0)

while True:
    success, img  = cap.read()
    img,bboxs = detector.findFaces(img)
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()     
cap.release()        
     