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
from calculate import Calculate
calc_obj =  Calculate()
from plotter import Plot
plotter_obj = Plot()



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
option = st.sidebar.radio('Select', ['About','QuakeView', 'QuakeEdu'])
# choosing what to do based on selected radio buttons
if option == 'QuakeView':
    st.sidebar.markdown('*Earthquake visualization on an interactive map*')
    st.header('QuakeView')
    # final = loader_obj.load_clean_data(response)

    city_date_option = st.sidebar.selectbox('Visualize On', ['Date', 'City/State'])
    if city_date_option == 'Date':
        date_option = st.sidebar.selectbox('Choose Dates', ['Today', 'This Week', 'This Month', 'This Year', 'Custom Date Range'])

        if date_option == 'Today':
            # btn = st.sidebar.button('Visualize')
            # if btn == True:
            response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(yesterday, today))
            final = loader_obj.load_clean_data(response)
            calc_obj.get_statistics(final)
            st.dataframe(final, use_container_width=True)
            st.subheader('Interactive Map')
            map_option = st.selectbox('Choose Map Style', ['Terrain', 'Light', 'Dark'])
            if map_option == 'Terrain':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Light':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Dark':
                plotter_obj.plot_iteractive_map(final, map_option)
            st.markdown('---')
            histogram_option = st.selectbox('Choose Histogram Style', ['Normal', 'Stacked'])
            if histogram_option == 'Normal':
                plotter_obj.plot_histogram(final, histogram_option)
            if histogram_option == 'Stacked':
                plotter_obj.plot_histogram(final, histogram_option)


        # String format used to put today's date and a date from week ago as params to the API
        if date_option == 'This Week':

            # btn = st.sidebar.button('Visualize', key='button')
            # if st.session_state['button'] == btn:
            response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(week_ago, today))
            final = loader_obj.load_clean_data(response)
            calc_obj.get_statistics(final)
            mag_slider = st.slider('Filer by magnitude', min_value= final['mag'].min(), max_value=final['mag'].max())
            final = final[final['mag'] > mag_slider]
            st.dataframe(final, use_container_width=True)
            # st.dataframe(final, use_container_width=True)
            st.subheader('Interactive Map')
            map_option = st.selectbox('Choose Map Style', ['Terrain', 'Light', 'Dark'])
            if map_option == 'Terrain':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Light':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Dark':
                plotter_obj.plot_iteractive_map(final, map_option)
            st.markdown('---')
            histogram_option = st.selectbox('Choose Histogram Style', ['Normal', 'Stacked'])
            if histogram_option == 'Normal':
                plotter_obj.plot_histogram(final, histogram_option)
            if histogram_option == 'Stacked':
                plotter_obj.plot_histogram(final, histogram_option)
        

        if date_option == 'This Month':
            # btn = st.sidebar.button('Visualize', key='button')
            # if st.session_state['button'] == btn:
            try:
                response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(first_day_month, today))
                final = loader_obj.load_clean_data(response)
                calc_obj.get_statistics(final)
                mag_slider = st.slider('Filer by magnitude', min_value= final['mag'].min(), max_value=final['mag'].max())
                final = final[final['mag'] > mag_slider]
                st.dataframe(final, use_container_width=True)
            except:
                st.warning('Please select the option labeled \'Today\' as it is the first day of the month.')
            st.subheader('Interactive Map')
            map_option = st.selectbox('Choose Map Style', ['Terrain', 'Light', 'Dark'])
            if map_option == 'Terrain':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Light':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Dark':
                plotter_obj.plot_iteractive_map(final, map_option)
            st.markdown('---')
            histogram_option = st.selectbox('Choose Histogram Style', ['Normal', 'Stacked'])
            if histogram_option == 'Normal':
                plotter_obj.plot_histogram(final, histogram_option)
            if histogram_option == 'Stacked':
                plotter_obj.plot_histogram(final, histogram_option)


        if date_option == 'This Year':
            # btn = st.sidebar.button('Visualize', key='button')
            # if st.session_state['button'] == btn:
            response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(year, today))
            final = loader_obj.load_clean_data(response)
            calc_obj.get_statistics(final)
            mag_slider = st.slider('Filer by magnitude', min_value= final['mag'].min(), max_value=final['mag'].max())
            final = final[final['mag'] > mag_slider]
            st.dataframe(final, use_container_width=True)
            st.subheader('Interactive Map')
            map_option = st.selectbox('Choose Map Style', ['Terrain', 'Light', 'Dark'])
            if map_option == 'Terrain':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Light':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Dark':
                plotter_obj.plot_iteractive_map(final, map_option)
            st.markdown('---')
            histogram_option = st.selectbox('Choose Histogram Style', ['Normal', 'Stacked'])
            if histogram_option == 'Normal':
                plotter_obj.plot_histogram(final, histogram_option)
            if histogram_option == 'Stacked':
                plotter_obj.plot_histogram(final, histogram_option)


        if date_option == 'Custom Date Range':
        #     btn = st.sidebar.button('Visualize', key='button')
            st.sidebar.markdown("<p style='color: orange;'>Note: If you select a wide range of dates that span several years, the data may not be displayed.</p>", unsafe_allow_html=True)
            start_date = st.date_input('Choose Start Date', max_value=today)
            end_date = st.date_input('Choose End Date', min_value=start_date, max_value=today)
            if end_date <= start_date:
                st.warning('Please choose an end date after the start date.')

            # if st.session_state['button'] == btn:   
            try: 
                response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(start_date, end_date))
                final = loader_obj.load_clean_data(response)
                calc_obj.get_statistics(final)
                mag_slider = st.slider('Filer by magnitude', min_value= final['mag'].min(), max_value=final['mag'].max())
                final = final[final['mag'] > mag_slider]
                st.dataframe(final, use_container_width=True)
                st.subheader('Interactive Map')
                map_option = st.selectbox('Choose Map Style', ['Terrain', 'Light', 'Dark'])
                if map_option == 'Terrain':
                    plotter_obj.plot_iteractive_map(final, map_option)
                if map_option == 'Light':
                    plotter_obj.plot_iteractive_map(final, map_option)
                if map_option == 'Dark':
                    plotter_obj.plot_iteractive_map(final, map_option)
                st.markdown('---')
                histogram_option = st.selectbox('Choose Histogram Style', ['Normal', 'Stacked'])
                if histogram_option == 'Normal':
                    plotter_obj.plot_histogram(final, histogram_option)
                if histogram_option == 'Stacked':
                    plotter_obj.plot_histogram(final, histogram_option)
            except:
                st.error('Data for the selected date range isn\'t available.')
    


    if city_date_option == 'City/State':
        response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=1-1-2015&endtime={}&minmagnitude=5'.format(today))
        final = loader_obj.load_clean_data(response)
        chosen_country = st.sidebar.selectbox('Choose the City/Country', sorted(list(final['city/state'].dropna().unique())))
        plotter_obj.plot_country(final, chosen_country)
            



if option == 'QuakeEdu':
    st.sidebar.markdown('*Learn earthquake preparedness tips and science behind seismic events*')


if option == 'About':
    st.sidebar.markdown('*Learn more about the project*')
    col1, col2 = st.columns(2)
    st.markdown("![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGI0ZWU5ZDcyM2FhOGE3NzVjZmQ2MzIxNzM3NGEyMmNlNmMyYWZjNSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/TdXeFkgX9nHqsZWkX0/giphy.gif)")
    st.markdown("![Alr Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNThhNjA5NjAyNmIyMDJhMWZjYWRhNWU3NWEwZDdhYjc2YmMzMjE2MCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/DfUB71qWDdDuIxk9U3/giphy.gif)")
    st.subheader('Introduction')
    st.write('Welcome to my earthquake plotting app! If you\'re anything like me, you\'re probably fascinated by the powerful forces of nature that can shake the ground beneath our feet. That\'s why I created this app - to help you explore and visualize earthquake data in a fun and interactive way!')
    st.write('With my app, you can easily plot earthquake data on a map and explore patterns and trends over time. Whether you\'re a seasoned geologist or just a curious beginner, this app is perfect for anyone who wants to learn more about earthquakes and their impact on the world.')
    st.write('So go ahead and give it a try! You might just discover something new and exciting about this amazing planet we call home.')
    st.markdown('---')

    st.subheader('Features of SiesmoStream')
    st.write('Hey there! So, in my app, you\'ll find some really cool visualizations that will help you explore earthquake data like never before!')
    st.write('- I\'ve created interactive maps that allow you to explore earthquakes by location. You can zoom in or out and click on any point to see the details of the earthquake that occurred at that location.')
    st.write('- But that\'s not all! I\'ve also created animations that show you how earthquakes have occurred over time. These animations give you a great perspective on how earthquakes have evolved over a specific period.')
    st.write('- I\'ve also included bar charts and line charts that show you how the frequency and magnitude of earthquakes have changed over time. This can help you identify patterns and trends in the occurrence of earthquakes.')
    