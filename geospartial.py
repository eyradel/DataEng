import streamlit as st
import folium
import ipywidgets
from folium import plugins
import geopy
import geocoder
import pandas as pd 
import numpy as np 
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            <html><body><p></p><body/></html>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

graph = folium.Map()
col1,col2 = st.columns(2)
with col1:
	st.write("dla")
with col2:
	st.write("dla")