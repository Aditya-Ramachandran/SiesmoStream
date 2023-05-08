import streamlit as st
import plotly.express as px

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