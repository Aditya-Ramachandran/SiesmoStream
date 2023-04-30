import pandas as pd
import datetime as dt
import requests
import numpy as np
from pandas import json_normalize
import datetime
import streamlit as st

st.header('SiesmoStream')
st.markdown('*SeismoStream: Because earthquakes aren\'t just for the birds.*')

# st.slider('hello')
# hitting the API and storing result in response variable
response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-04-28&endtime=2023-04-29&minmagnitude=5')


st.sidebar.header('SiesmoStream')
option = st.sidebar.radio('Select', ['QuakeView', 'QuakeEdu', 'About'])

# choosing what to do based on selected radio buttons
if option == 'QuakeView':
    st.sidebar.markdown('*Earthquake visualization on an interactive map*')


if option == 'QuakeEdu':
    st.sidebar.markdown('*Learn earthquake preparedness tips and science behind seismic events*')


if option == 'About':
    st.sidebar.markdown('*Learn more about the project*')
