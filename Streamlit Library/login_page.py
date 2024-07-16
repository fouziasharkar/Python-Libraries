import streamlit as st



email = st.text_input('Email')
password = st.text_input('Password')

#dropdown
gender = st.selectbox('Select Gender', ['Select','Male','Female','Others'])

btn = st.button('Login')

if btn:
    if email=='Fouzia' and password=='123456':
        st.success('Login Successful')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Unsuccessful')

