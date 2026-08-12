import streamlit as st

# write the header
st.header("User input demo")

# write subheader
st.subheader("different ways to get input from user")

# get single line input from user
title = st.text_input("todo item title here")

# get multi line input from user
description = st.text_area("todo item description here")

# get date input from user
birth_date = st.date_input("select your birth date")

# get time input from user
time = st.time_input("select birth time")

# get the input using dropdown
city = st.selectbox('Select city', ['pune', 'mumbai', 'bengloru'])