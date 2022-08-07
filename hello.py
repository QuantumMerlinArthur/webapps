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

import plotly.figure_factory as ff
import numpy as np

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)
