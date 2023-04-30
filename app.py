import pandas as pd
import datetime as dt
import requests
import numpy as np
from pandas import json_normalize
import datetime
import streamlit as st

from loader import GetDataFromAPI
loader_obj = GetDataFromAPI()


st.header('SiesmoStream')
st.markdown('*SeismoStream: Because earthquakes aren\'t just for the birds.*')
st.markdown('---')

# st.slider('hello')
# hitting the API and storing result in response variable
response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-04-29&endtime=2023-04-30&minmagnitude=5')


st.sidebar.header('SiesmoStream')
option = st.sidebar.radio('Select', ['QuakeView', 'QuakeEdu', 'About'])

# choosing what to do based on selected radio buttons
if option == 'QuakeView':
    st.sidebar.markdown('*Earthquake visualization on an interactive map*')
    st.header('QuakeView')
    loader_obj.load_clean_data(response)

    



if option == 'QuakeEdu':
    st.sidebar.markdown('*Learn earthquake preparedness tips and science behind seismic events*')


if option == 'About':
    st.sidebar.markdown('*Learn more about the project*')
