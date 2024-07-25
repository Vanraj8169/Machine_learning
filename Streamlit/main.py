import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title("Hello Streamlit")

# Display a simple text
st.write("This is a simple text")

df = pd.DataFrame({
    'first column': [10,30,20,40],
    'second column': [10,20,30,40]
})

# Display the DataFrame
st.write("Here is the DataFrame")
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)