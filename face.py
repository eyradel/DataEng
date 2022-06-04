import streamlit as st
import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector
detector = FaceDetector()
video = cv.VideoCapture(0)
run = st.button("trigger")
frame = st.image([])
while run:
	success,capture = video.read()
	
	img,bboxs = detector.findFaces(capture)
	capture = cv.cvtColor(capture,cv.COLOR_BGR2RGB)

	Blur = cv.GaussianBlur(capture,(5,5),2)
	
	#frame.image(capture)
	frame.image(Blur)
stop = st.button("stop")

if stop:
	cv.destroyAllWindows()
	video.release()



