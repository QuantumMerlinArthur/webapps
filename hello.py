import streamlit as st
import pandas as pd
st.title("18 questions")
name = st.text_input("Enter your name", "")

st.write(f"Hello {name}!")

val=st.button('Click me')
st.write(f"Button value:{val}")
st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size



x = st.slider("Select an integer x", 0, 10, 1)
y = st.slider("Select an integer y", 0, 10, 1)
df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
st.write(df)
