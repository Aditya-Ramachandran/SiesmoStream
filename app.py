import pandas as pd
import datetime as dt
import requests
import numpy as np
from pandas import json_normalize
import datetime
import streamlit as st
from datetime import date


from loader import GetDataFromAPI
loader_obj = GetDataFromAPI()


st.set_page_config(layout='wide', page_title='SiesmoStream')

st.header('SiesmoStream')
st.markdown('*SeismoStream: Because earthquakes aren\'t just for the birds.*')
st.markdown('---')

# st.slider('hello')
# hitting the API and storing result in response variable
# response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-04-29&endtime=2023-04-30&minmagnitude=5')

today = dt.date.today()
week_ago = today - dt.timedelta(days=7)
yesterday = today - dt.timedelta(days=1)
first_day_month = today.replace(day=1)
year = date(date.today().year, 1, 1)



st.sidebar.header('SiesmoStream')
option = st.sidebar.radio('Select', ['QuakeView', 'QuakeEdu', 'About'])

# choosing what to do based on selected radio buttons
if option == 'QuakeView':
    st.sidebar.markdown('*Earthquake visualization on an interactive map*')
    st.header('QuakeView')
    # final = loader_obj.load_clean_data(response)

    city_date_option = st.sidebar.selectbox('Visualize On', ['Date', 'City/State'])
    if city_date_option == 'Date':
        date_option = st.sidebar.selectbox('Choose Dates', ['Today', 'This Week', 'This Month', 'This Year', 'Custom Date Range'])

        if date_option == 'Today':
            btn = st.sidebar.button('Visualize')
            if btn == True:
                response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(yesterday, today))
                loader_obj.load_clean_data(response)

        # String format used to put today's date and a date from week ago as params to the API
        if date_option == 'This Week':
            btn = st.sidebar.button('Visualize')
            if btn == True:
                response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(week_ago, today))
                loader_obj.load_clean_data(response)
        
        if date_option == 'This Month':
            btn = st.sidebar.button('Visualize')
            if btn == True:
                response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(first_day_month, today))
                loader_obj.load_clean_data(response)

        if date_option == 'This Year':
            btn = st.sidebar.button('Visualize')
            if btn == True:
                response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(year, today))
                loader_obj.load_clean_data(response)

        if date_option == 'Custom Date Range':
            btn = st.sidebar.button('Visualize')
            st.sidebar.markdown("<p style='color: orange;'>Note: If you select a wide range of dates that span several years, the data may not be displayed.</p>", unsafe_allow_html=True)
            start_date = st.date_input('Choose Start Date', max_value=today)
            end_date = st.date_input('Choose End Date', min_value=start_date, max_value=today)
            if end_date <= start_date:
                st.warning('Please choose an end date after the start date.')

            if btn == True:   
                try: 
                    response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(start_date, end_date))
                    loader_obj.load_clean_data(response)
                except:
                    st.error('Data for the selected date range isn\'t available.')
        





    



if option == 'QuakeEdu':
    st.sidebar.markdown('*Learn earthquake preparedness tips and science behind seismic events*')


if option == 'About':
    st.sidebar.markdown('*Learn more about the project*')
