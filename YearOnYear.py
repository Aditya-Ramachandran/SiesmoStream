import streamlit as st
import plotly.express as px
import pandas as pd


from loader import GetDataFromAPI
loader_obj = GetDataFromAPI()



class YearOnYear:

    def __init__(self) -> None:
        pass

    def plot_yoy_bar(self, dataframe):
        temp_df = dataframe.groupby('Year')['mag'].count().reset_index()
        temp_df.rename(columns={'mag':'Count'}, inplace=True)
        fig = px.bar(temp_df, x='Year', y='Count', color='Count')
        fig.update_layout(xaxis=dict(dtick='1 year'), xaxis_title='Year', yaxis_title='Count', title='Earthquakes by Year - Bar Chart')
        st.plotly_chart(fig,use_container_width=True)
    
    def plot_yoy_line(self, dataframe):
        temp_df = dataframe.groupby('Year')['mag'].count().reset_index()
        temp_df.rename(columns={'mag':'Count'}, inplace=True)
        fig = px.line(temp_df, x='Year', y='Count', markers='o')
        fig.update_layout(xaxis=dict(dtick='1 year'), xaxis_title='Year', yaxis_title='Count',yaxis=dict(range=[1100,2500]),title='Earthquakes by Year - Line Chart')
        st.plotly_chart(fig,use_container_width=True)

    def plot_yoy_animated_graph(self, dataframe):
        dataframe = dataframe.sort_values(by='Year')
        fig = px.density_mapbox(dataframe, lat='Latitude', lon='Longitude', z='mag', radius=10,
                        center=dict(lat=0, lon=180), zoom=0.5,
                        mapbox_style= 'stamen-terrain',height=700 ,color_continuous_scale=px.colors.sequential.Plasma, animation_frame='Year', title='Animated Graph')
        st.plotly_chart(fig,use_container_width=True)