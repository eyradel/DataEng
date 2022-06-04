# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:12:44 2022

@author: Delaeyram
"""

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import streamlit as st
st.title("WebCam object Detector")
st.balloons()
st.markdown("Built by Eyram Dela")
run = st.checkbox("Run")
FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(0)
while run:
    sucess,frame =cam.read()
    bbox,label,conf = cv.detect_common_objects(frame)
    out = draw_bbox(frame,bbox,label,conf)
    FRAME_WINDOW.image(frame)
else:
    st.write("stop")
