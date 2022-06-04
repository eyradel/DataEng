import streamlit as st
st.title("hello")
st.header("hi")
st.subheader("hello there")
st.markdown("dela here")
st.success("successful")
st.info("information")
st.warning("warning")
st.error("error")
st.exception("NameError('name three not defined')")
st.help(range)
st.write("Text with write")
st.write(range(10))

from PIL import Image
img = Image.open(r"C:\Users\Delaeyram\Downloads\WhatsApp Image 2022-05-07 at 4.18.44 PM.jpeg")
st.image(img,width=300,caption="image")

vid = open(r"C:\Users\Delaeyram\Downloads\Spirit Of Praise 5 feat. Zaza - Ngena.mp4","rb").read()
st.video(vid)

audio = open(r"C:\Users\Delaeyram\Downloads\Spirit Of Praise 5 feat. Zaza - Ngena.mp4","rb").read()
st.audio(audio,format="audio/mp3")
if st.checkbox("Show/Hide"):
    st.text("showing or hiding widget")
status = st.radio("what is the status",("Active","Inactive"))
if status =="Active":
    st.success("You are active")
else:
    st.warning("Inactive,Activate")
occupation = st.selectbox("Your Occupation",["programmer","data scientist","Doctor"])
st.write("You selected ",occupation)
location = st.multiselect("where do you work",("london","accra","uk"))
st.write("you selected",len(location),"locations")
level = st.slider("what is your level",1,5)
st.button("simple button")
if st.button("About"):
    st.text("cool")
    
firstname = st.text_input("enter your name","Type here ")
if st.button("submit"):
    result = firstname.title()
    st.success(result)
    
    
message = st.text_area("enter your name","Type here ")
if st.button("send"):
    result = message.title()
    st.success(result)
    
import datetime
today = st.date_input("todays date",datetime.datetime.now())
time = st.time_input("the time is",datetime.time())
st.text("Display json")
st.json({'name':"jesse",'gender':"male"})
st.text("Display raw code")
st.code("import numpy as np")
with st.echo():
    import pandas as pd
    df = pd.DataFrame()
import time
mybar = st.progress(0)
for p in range(10):
    mybar.progress(p+1)
    
with st.spinner("waiting......"):
    time.sleep(5)
st.success("Finished")
st.balloons()


st.sidebar.header("About")
st.sidebar.text("this is streamlit")
st.snow()
@st.cache
def run_fxn():
    return range(100)
st.write(run_fxn())    

st.pyplot()


from streamlit_webrtc import webrtc_streamer
webrtc_streamer(key="key")

