import streamlit as st
import pandas as pd

file = st.file_uploader('Upload your file')


if file is not None:
    rd = pd.read_csv(file)
    df = pd.DataFrame(rd)

    st.write(df.describe())