import pandas as pd
import scipy.stats
import streamlit as st
import plotly.express as px

vehicles_df = pd.read_csv('vehicles_us.csv')

#Here I took the average model_year to have an approximation to fill the missing NaN years.
year_mean = vehicles_df['model_year'].mean().round()

#Now it's time to address the missing values. That is done below.
vehicles_df['model_year'] = vehicles_df['model_year'].fillna(year_mean)
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].fillna(0.0)
vehicles_df['paint_color'] = vehicles_df['paint_color'].fillna('Not Available')
vehicles_df['odometer'] = vehicles_df['odometer'].fillna(0)

#In this next section, I will be removing outliers so the charts are more consise and readable.
Q1_year = vehicles_df['model_year'].quantile(0.25)
Q3_year = vehicles_df['model_year'].quantile(0.75)
IRQ_year = Q3_year - Q1_year

Q1_price = vehicles_df['price'].quantile(0.25)
Q3_price = vehicles_df['price'].quantile(0.75)
IRQ_price = Q3_price - Q1_price

Q1_miles = vehicles_df['odometer'].quantile(0.25)
Q3_miles = vehicles_df['odometer'].quantile(0.75)
IRQ_miles = Q3_miles - Q1_miles

vehicles_df = vehicles_df[
    (vehicles_df['model_year'] >= (Q1_year - 1.5 * IRQ_year)) & 
    (vehicles_df['model_year'] <= (Q3_year + 1.5 * IRQ_year)) &
    (vehicles_df['price'] >= (Q1_price - 1.5 * IRQ_price)) & 
    (vehicles_df['price'] <= (Q3_price + 1.5 * IRQ_price)) &
    (vehicles_df['odometer'] >= (Q1_miles - 1.5 * IRQ_miles)) & 
    (vehicles_df['odometer'] <= (Q3_miles + 1.5 * IRQ_miles))
]

vehicles_df = vehicles_df.rename(columns={'price': 'Price($)', 'model_year': 'Year', 'model': 'Make/Model', 'condition': 'Condition', 'cylinders': 'Cylinders', 'fuel': 'Fuel', 'odometer': 'Odometer', 'type': 'Type', 'paint_color': 'Paint', 'is_4wd': '4WD', 'date_posted': 'Date Posted', 'days_listed': 'Days Listed'})


st.header('Charts for Cars')

st.subheader('Data Summary')
col1, col2, col3 = st.columns(3)
col1.metric("Total Vehicles", len(vehicles_df_w_odometer))
col2.metric("Average Price", f"${vehicles_df_w_odometer['Price($)'].mean():.2f}")
col3.metric("Average Year", f"{vehicles_df_w_odometer['Year'].mean():.1f}")

fig_hist = px.histogram(vehicles_df, x='Price($)', nbins=30, title='Distribution of Vehicle Prices')
st.plotly_chart(fig_hist)

fig_scatter = px.scatter(vehicles_df, x='Odometer', y='Price($)', title='Price Vs Odometer')
st.plotly_chart(fig_scatter)

if st.checkbox('Show Dataframe'):
  st.write(vehicles_df)
