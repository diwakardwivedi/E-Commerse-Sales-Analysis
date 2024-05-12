import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

path = os.path.join(os.getcwd(), 'Superstore.xlsx')

df = pd.read_excel(path)
st.write(df)

fig = px.bar(df.head(100),x='City', y='Sales',color='Category',width=700,title='maximum and minimum sales in cities')
st.plotly_chart(fig)

fig = px.bar(df.head(20),x='Customer Name',y='Quantity'
             ,color='Profit',
             hover_data=['Discount','Product Name','Sub-Category'],
             width=1000,title='Product with quantity purchased by Customer')
st.plotly_chart(fig)

fig =px.pie(df,names='Sub-Category',values='Profit',title='Sub-Categories with profit using pie chart')
st.plotly_chart(fig)


