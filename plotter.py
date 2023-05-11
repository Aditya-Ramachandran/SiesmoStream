import streamlit as st
import plotly.express as px
import datetime as dt
import requests

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