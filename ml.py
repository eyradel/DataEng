import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn import linear_model
df = pd.read_excel(r"C:\Users\Delaeyram\Downloads\Edward data.xlsx")
fig, ax = plt.subplots()
plt.scatter(df['length'],df['width'])
st.pyplot()
reg = linear_model.LinearRegression()
reg.fit(df[['height','width']],df.length)
reg.coef_
reg.intercept_
st.write("final multi variate formulae")
st.write("formulae format is "," length = X*height + y*width  + intercept(constant)")
st.write("length =",str(5.13743898),"h ",float(-0.70296658),"w"," + ",int(-122.90311678557987))


from matplotlib_venn import venn2
venn2(subsets = (5,8,5),set_labels =("boy","girl"))
plt.show()
st.pyplot()