import streamlit as st
import plotly.express as px
import datetime as dt
import requests
import pandas as pd

from YearOnYear import YearOnYear
yoy_obj = YearOnYear()
from loader import GetDataFromAPI
loader_obj = GetDataFromAPI()

today = dt.date.today()

class Plot:

    def __init__(self) -> None:
        pass

    def plot_iteractive_map(self, dataframe, option):
        if option == 'Terrain':
            mapbox_style = 'stamen-terrain'
        if option == 'Light':
            mapbox_style = 'carto-positron'
        if option == 'Dark':
            mapbox_style = 'carto-darkmatter'
        fig = px.density_mapbox(dataframe, lat='Latitude', lon='Longitude', z='mag', radius=10,
                        center=dict(lat=0, lon=180), zoom=0.5,
                        mapbox_style= mapbox_style,height=700 ,color_continuous_scale=px.colors.sequential.Plasma,
                        hover_name='place')
        st.plotly_chart(fig, use_container_width=True)
    

    def plot_histogram(self, dataframe, option):
        st.subheader('Histogram')
        # fig = px.bar(dataframe, x='city/state', y='mag', hover_name='city/state')
        if option == 'Normal':
            fig = px.histogram(dataframe, x='city/state')
            st.plotly_chart(fig, use_container_width=True)
        if option == 'Stacked':
            if dataframe['place'].value_counts().head(1).values[0] > 1:
                fig = px.histogram(dataframe, x='city/state',color='mag')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning('Too little data for a stacked histogram')
        st.markdown('---')

        st.subheader('Year on Year statistics')
        st.write('Discover the fascinating Year on Year statistics with stunning visuals and mesmerizing animations that will leave you captivated. Dive into the data and unravel insights that will surprise you.')
        st.write('*Please note that due to the size of the data, some graphs may take a few seconds to load, but trust me, it\'s worth the wait!*')
        btn = st.button('See Year on Year stats')  
        # col1, col2 = st.colums(2)
        if btn:
            response1 = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-3-3&endtime=2023-1-1&minmagnitude=5')
            final1 = loader_obj.load_clean_data(response1)
            col1, col2 = st.columns(2)
            
            yoy_obj.plot_yoy_bar(final1)
            
            yoy_obj.plot_yoy_line(final1)

            yoy_obj.plot_yoy_animated_graph(final1)

            with col1:
                yoy_obj.plot_pie_total(final1)


    def plot_country(self, dataframe, choice):
        
        try:
            url = 'https://api.opencagedata.com/geocode/v1/geojson?q={}&key=028fc01b3e044c1693027b167e31b1b5&pretty=1'.format(choice)
            response = requests.get(url)
        except:
            st.warning('Data could not be loaded')
        lat = response.json()['features'][0]['geometry']['coordinates'][0]
        lon = response.json()['features'][0]['geometry']['coordinates'][1]
        curr_name = response.json()['features'][0]['properties']['annotations']['currency']['name']
        smallest_denomination =  response.json()['features'][0]['properties']['annotations']['currency']['smallest_denomination']
        drive = response.json()['features'][0]['properties']['annotations']['roadinfo']['drive_on']
        speed_in = response.json()['features'][0]['properties']['annotations']['roadinfo']['speed_in']
        timezone = response.json()['features'][0]['properties']['annotations']['timezone']['name']
        GMT_relative = response.json()['features'][0]['properties']['annotations']['timezone']['offset_string']

        new_df = pd.DataFrame({'Longitude': [lat], 'Latitude': [lon], 'Currency': [curr_name], 'Smallest Denomination': [smallest_denomination],
                        'Driving Side': [drive], 'Speed Unit':[speed_in], 'Timezone':timezone, 'Relative to GMT':GMT_relative, 'Country':choice})
        
        st.subheader('Some stats about {}'.format(choice))
        col1, col2 = st.columns(2)
        with col1:
            st.metric('Currency Name', curr_name)
            st.metric('Driving Side', drive)
            st.metric('Timezone Name',timezone )
        with col2:
            st.metric('Smallest Denomination', smallest_denomination)
            st.metric('Speed Measured in', speed_in)
            st.metric('Relative to GMT', GMT_relative)
        
        # st.dataframe(new_df, use_container_width=True)
        fig = px.scatter_geo(new_df, lat='Latitude', lon='Longitude', projection='mollweide', title='{} on World Map'.format(choice), height=550, hover_name='Country')   
        fig.update_traces(marker=dict(size=15))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('---')

        yoy_obj.plot_country_bar_chart(dataframe, choice)

        yoy_obj.plot_country_bar_chart_month(dataframe, choice)