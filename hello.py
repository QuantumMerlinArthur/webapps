import streamlit as st
import pandas as pd
st.title("18 questions")
name = st.text_input("Enter your name", "")

st.write(f"Hello {name}!")



st.checkbox('I agree')
val=st.radio('Choose favourite pet', ['cats', 'dogs','guinea pigs'])
st.write(f"user input value: {val}")

dict = {"cats":0,"dogs":1,"guinea pigs":2}

#st.write(f"array index: {dict[val]}")
st.button('Save answer',key="save")

poll=[0,0,0]
if st.session_state.save:
  poll[dict[val]]+=1

# plotting example
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)

data = [23, 45, 56]
fig, ax = plt.subplots()
ax.bar(['cats', 'dogs','guinea pigs'], poll)
#ax.hist(arr, bins=20)

st.pyplot(fig)
