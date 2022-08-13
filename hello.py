import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# database sql
import mysql.connector
mysql.connector.connect(host='https.//remotemysql.com:3306',database='QtbVDcLbg8',user='QtbVDcLbg8',password='EO3VPt1koW')

##### main page
st.title("18 questions")

val=st.radio('Choose favourite pet', ['cats', 'dogs','guinea pigs'])
st.write(f"user input value: {val}")

dict = {"cats":0,"dogs":1,"guinea pigs":2}

#st.write(f"array index: {dict[val]}")
st.button('Save answer',key="save")

poll=np.arange(0.0,5.0,1.0)
if st.session_state.save:
  
  poll[dict[val]]+=1
  np.savetxt("poll.txt",poll)
  st.write(">>Saved")

# plotting example

data = [23, 45, 56]
fig, ax = plt.subplots()
ax.bar(['cats', 'dogs','guinea pigs'], data)
st.pyplot(fig)
