import streamlit as st
import pandas

data = {"Stream 1" : [1, 2, 4, 5, 6, 7],
        "Stream 2" : [23, 34, 56, 45, 60, 79]}

df = pandas.DataFrame(data)

st.title("First Streamlit Web App")
st.subheader("Simple App")
st.write("""Brought to you by Pris.
Enjoy!""")
st.write(df)