import streamlit as st
import pandas as pd

# load the data
df = pd.read_csv('Salary_Data.csv')

# show the header
st.header("My Website")

# show the subheader
st.subheader("This is simple website demo")

# write the contents on the UI
st.write("""Streamlit is more than just a way to make data apps, it's also a community of creators that share their apps and ideas and help each other make their work better. Please come join us on the community forum. We love to hear your questions, ideas, and help you work through your bugs — stop by today!""")

# write the data frame
st.subheader("Pandas Dataframe")
st.write(df)

# create a line chart
st.subheader("Line Chart")
st.line_chart(df)
