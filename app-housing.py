import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('seaborn')
housing_df = pd.read_csv('housing.csv')

st.title('California Housing Data(1990) by Man Wang')

price_filter = st.slider('Median House Price(minimal)', 0.0, 500001.0, 200000.0)

st.header('See more filters in the sidebar:')

locate_filter = st.sidebar.multiselect(
    'Choose the location type',
    housing_df.ocean_proximity.unique(),
    housing_df.ocean_proximity.unique(),
    )

income_filter = st.sidebar.radio('Choose income level', ['low', 'median', 'high'])

housing_df = housing_df[housing_df.median_house_value <= price_filter]
housing_df = housing_df[housing_df.ocean_proximity.isin(locate_filter)]

if income_filter == 'low':
    housing_df = housing_df[housing_df.median_income <= 2.5]
elif income_filter == 'median':
    housing_df = housing_df[housing_df.median_income > 2.5]
    housing_df = housing_df[housing_df.median_income < 4.5]
elif income_filter == 'high':
    housing_df = housing_df[housing_df.median_income >= 4.5]

st.map(housing_df)

fig, ax = plt.subplots()
housing_df.median_house_value.hist(bins=30)

st.header('Histgram of median house value')
st.pyplot(fig)