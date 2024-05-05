import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

st.title('My Dashboard')
file = st.file_uploader('Upload a file', type=['csv', 'xlsx'])

if file is not None:
    st.write(file.name)

    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        st.write('File type not supported')
    st.write(df)
else:
    st.write('No file uploaded')

