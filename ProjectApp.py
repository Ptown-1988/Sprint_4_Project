import pandas as pd
import scipy.stats
import streamlit as st
import plotly.express as px

vehicles_df = pd.read_csv('vehicles_us.csv')

year_mean = vehicles_df['model_year'].mean()

vehicles_df['model_year'] = vehicles_df['model_year'].fillna(2009)
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].fillna(0.0)
vehicles_df['paint_color'] = vehicles_df['paint_color'].fillna('Not Available')
vehicles_df_w_odometer = vehicles_df.dropna(subset=['odometer'])

#Vehicles without an accurate odometer reading have been removed from the vehicle advertisment list

Q1_year = vehicles_df_w_odometer['model_year'].quantile(0.25)
Q3_year = vehicles_df_w_odometer['model_year'].quantile(0.75)
IRQ_year = Q3_year - Q1_year

Q1_price = vehicles_df_w_odometer['price'].quantile(0.25)
Q3_price = vehicles_df_w_odometer['price'].quantile(0.75)
IRQ_price = Q3_price - Q1_price

Q1_miles = vehicles_df_w_odometer['odometer'].quantile(0.25)
Q3_miles = vehicles_df_w_odometer['odometer'].quantile(0.75)
IRQ_miles = Q3_miles - Q1_miles

vehicles_df_w_odometer = vehicles_df_w_odometer[~((vehicles_df_w_odometer['model_year'] < (Q1_year - 1.5 * IRQ_year)) | (vehicles_df_w_odometer['model_year'] > (Q3_year + 1.5 * IRQ_year)))]
vehicles_df_w_odometer = vehicles_df_w_odometer[~((vehicles_df_w_odometer['price'] < (Q1_price - 1.5 * IRQ_price)) | (vehicles_df_w_odometer['price'] > (Q3_price + 1.5 * IRQ_price)))]
vehicles_df_w_odometer = vehicles_df_w_odometer[~((vehicles_df_w_odometer['odometer'] < (Q1_miles - 1.5 * IRQ_miles)) | (vehicles_df_w_odometer['odometer'] > (Q3_miles + 1.5 *IRQ_miles)))]

vehicles_df_w_odometer = vehicles_df_w_odometer.rename(columns={'price': 'Price($)', 'model_year': 'Year', 'model': 'Make/Model', 'condition': 'Condition', 'cylinders': 'Cylinders', 'fuel': 'Fuel', 'odometer': 'Odometer', 'type': 'Type', 'paint_color': 'Paint', 'is_4wd': '4WD', 'date_posted': 'Date Posted', 'days_listed': 'Days Listed'})

st.header('Charts for Cars')

fig_hist = px.histogram(vehicles_df_w_odometer, x='Price($)', nbins=30, title='Distribution of Vehicle Prices')
st.plotly_chart(fig_hist)

fig_scatter = px.scatter(vehicles_df_w_odometer, x='Odometer (Miles)', y='Price($)', title='Price Vs Odometer')
st.plotly_chart(fig_scatter)

if st.checkbox('Show Dataframe'):
  st.write(vehicles_df_w_odometer)
