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

# st.write(response.json())