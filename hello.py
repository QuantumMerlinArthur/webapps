import streamlit as st
import pandas as pd
st.title("18 questions")
name = st.text_input("Enter your name", "")

st.write(f"Hello {name}!")

st.button('Click me')

st.checkbox('I agree')
val=st.radio('Pick one', ['cats', 'dogs'])
st.write(f"user input value:{val}")


# plotting example
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
