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
        st.plotly_chart(fig)
    
    def plot_yoy_line(self, dataframe):
        temp_df = dataframe.groupby('Year')['mag'].count().reset_index()
        temp_df.rename(columns={'mag':'Count'}, inplace=True)
        fig = px.line(temp_df, x='Year', y='Count', markers='o')
        fig.update_layout(xaxis=dict(dtick='1 year'), xaxis_title='Year', yaxis_title='Count',yaxis=dict(range=[1100,2500]),title='Earthquakes by Year - Line Chart')
        st.plotly_chart(fig)