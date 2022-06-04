import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config("Regression","")
def linear():
    file = st.text_input("Paste File path without quotation")
    data = pd.read_csv(str(file))
    if st.checkbox("plot"):
        data.plot
    st.dataframe(data)
    x = st.text_input("input column name for x")
    y = st.text_input("input column name for y")

def multivariate():
    st.file_uploader("upload Datasheet",["csv"])
st.sidebar.title("Sidebar")
tp = st.sidebar.selectbox("Type",["Linear","Multivariate"])
if tp=="Linear":
    st.markdown("Linear Regression")
    linear()
elif tp=="Multivariate":
    st.markdown("Multivariate regression")
    multivariate()
