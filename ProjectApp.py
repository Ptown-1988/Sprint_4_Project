import pandas as pd
import scipy.stats
import streamlit as st
import plotly.express as px

vehicles_df = pd.read_csv('vehicles_us.csv')

st.header('Charts for Cars', anchor=None, *, help=None, divider='blue')

st.plotly_chart(plt.figure(figsize=(10, 6))
plt.hist(vehicles_df_w_odometer['Price($)'], bins=30, edgecolor='black')
plt.title('Distribution of Vehicle Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show(), use_container_width=True, *, theme="streamlit", key=None, on_select="ignore", selection_mode=('points', 'box', 'lasso'), **kwargs)

st.plotly_chart(plt.figure(figsize=(10, 6))
plt.scatter(vehicles_df_w_odometer['Odometer'], vehicles_df_w_odometer['Price($)'], alpha=0.5)
plt.title('Scatterplot of Price vs Odometer')
plt.xlabel('Odometer (Miles)')
plt.ylabel('Price')
plt.show(), use_container_width=True, *, theme="streamlit", key=None, on_select="ignore", selection_mode=('points', 'box', 'lasso'), **kwargs)

st.checkbox('Chart Type', value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
