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
    
    def plot_pie_total(self, dataframe):
        temp_df = dataframe.groupby('Year')['mag'].count().reset_index()
        temp_df.rename(columns={'mag':'Count'}, inplace=True)
        fig = px.pie(temp_df, values='Count', names='Year', title='Count of Earthquakes in the Last 10 Years - Pie Chart', labels='Year')
        st.plotly_chart(fig)
    

    def plot_country_bar_chart(self, dataframe, choice):
        temp_df = dataframe[dataframe['city/state'] == choice].groupby('Year')['mag'].count().reset_index()
        temp_df.rename(columns={'mag':'Count'}, inplace=True)
        fig = px.bar(temp_df, x='Year', y='Count', color='Count')
        fig.update_layout(xaxis=dict(dtick='1 year'), xaxis_title='Year', yaxis_title='Count', title='Earthquakes in {} by Year - Bar Chart'.format(choice))
        st.plotly_chart(fig, use_container_width=True)
    
    def plot_country_bar_chart_month(self, dataframe, choice):
        temp_df = dataframe[dataframe['city/state'] == choice].groupby(dataframe['Date'].dt.month_name())['mag'].count().sort_values(ascending=False).reset_index()
        temp_df.rename(columns={'mag':'Count', 'Date':'Month'}, inplace=True)
        fig = px.bar(temp_df, x='Month', y='Count', color='Count')
        fig.update_layout(xaxis_title='Month', yaxis_title='Count', title='Earthquakes in {} by Month - Bar Chart'.format(choice))
        st.plotly_chart(fig, use_container_width=True)
    


    def plot_country_pie_chart_overall(self, dataframe, choice):
        temp_df = dataframe[dataframe['city/state'] == choice].groupby('Year')['mag'].count().reset_index()
        temp_df.rename(columns={'mag':'Count'}, inplace=True)
        fig = px.pie(temp_df, values='Count', names='Year', title='All Earthquakes by Year - Pie Chart')
        st.plotly_chart(fig)

    def plot_country_pie_chart_month(self, dataframe, choice):
        temp_df = dataframe[dataframe['city/state'] == choice].groupby(dataframe['Date'].dt.month_name())['mag'].count().sort_values(ascending=False).reset_index()
        temp_df.rename(columns={'mag':'Count', 'Date':'Month'}, inplace=True)
        fig = px.pie(temp_df, values='Count', names='Month', title='All Earthquakes by Month - Pie Chart')
        st.plotly_chart(fig)

        # st.dataframe(temp_df)

    
    
