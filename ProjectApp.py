import pandas as pd
import scipy.stats
import streamlit as st
import plotly.express as px

vehicles_df = pd.read_csv('vehicles_us.csv')

st.header('Charts for Cars')

fig_hist = px.hist(vehicles_df_w_odometer, x='Price($)', bins=30, title='Distribution of Vehicle Prices', xlabel='Price', ylabel='Frequency', edgecolor='black')
st.plotly_chart(fig_hist)

fig_scatter = px.scatter(vehicles_df_w_odometer, x='Odometer (Miles)', y='Price($)', title='Price Vs Odometer', xlabel='Odometer (Miles)', ylabel='Price')
st.plotly_chart(fig_scatter)

if st.checkbox('Show Dataframe'):
  st.write(vehicles_df_w_odometer)
