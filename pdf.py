import streamlit as st
#import PyPDF2  as pdf
import pyttsx3
engine = pyttsx3.init()
voice = engine.getProperty('voices')

engine.setProperty("voice", voice[0].id)
@st.cache()
def read(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
    
text = st.text_input("input a text")
if st.button("play"):
    read(text)
else:
    engine.stop()    



#file = open("C:/Users/kuwor/Documents/Artificial Intelligence with Python.pdf",'rb')


# reader = pdf.PdfFileReader(file)
# print(reader.numPages)
# for x in range(0,int(reader.numPages),1):    
#     page = reader.getPage(x)
#     print(page.extractText())
#     read(page.extractText())
    
# file.close()