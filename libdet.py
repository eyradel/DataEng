import streamlit as st
import cv2
from PIL import Image
import numpy as np
import cvlib as cv
from cvlib.object_detection import draw_bbox

st.title("Multi detector")
st.markdown("Author Eyram Dela")


uploaded_file = st.file_uploader("Choose a file", type =['jpg','jpeg','jfif','png'])
image = np.array(Image.open(uploaded_file))
bbox,label,conf = cv.detect_common_objects(image)
out = draw_bbox(image,bbox,label,conf)
if st.checkbox("output"):
    

    
    placeholders = st.columns(1)
    placeholders[0].image(out)
if st.checkbox("Gray"):
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    placeholders = st.columns(1)
    placeholders[0].image(image)
if st.checkbox("objects"):
    st.write("Objects Detected",label)
    objects = str(label)
    st.write(objects)    