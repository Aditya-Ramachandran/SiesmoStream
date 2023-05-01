import pandas as pd
import datetime as dt
import requests
import numpy as np
from pandas import json_normalize
import datetime
import streamlit as st

from calculate import Calculate
calc_obj =  Calculate()


class GetDataFromAPI:

    def __init__(self) -> None:
        pass;

    # loads API data, cleans it into a nice DF which can be used for plotting
    def load_clean_data(self, data):
        '''
        This method takes in earthquake data in JSON format, cleans and normalizes it, 
        and returns a Pandas DataFrame with relevant columns.
        
        Parameters:
            data (json): JSON object containing earthquake data
            
        Returns:
            DataFrame: A Pandas DataFrame with columns 'mag', 'place', 'Latitude', 'Longitude' and 'city/state'
        '''
        properties = pd.DataFrame(data.json()['features'])['properties']
        geometry = pd.DataFrame(data.json()['features'])['geometry']
        json_normalized_properties = json_normalize(properties)
        json_normalized_geometry = json_normalize(geometry)
        json_normalized_properties = json_normalized_properties[['mag', 'place']]
        json_normalized_geometry['Latitude'] = json_normalized_geometry['coordinates'].str.get(0)
        json_normalized_geometry['Longitude'] = json_normalized_geometry['coordinates'].str.get(1)
        json_normalized_geometry.drop(columns=['type','coordinates'], inplace=True)
        final = pd.concat([json_normalized_properties, json_normalized_geometry], axis=1)
        final['city/state'] = final['place'].str.split(',').str.get(1)
        final['place'] = final['place'].str.split(',').str.get(0)
        final.rename(columns={'Latitude':'Longitude', 'Longitude':'Latitude'}, inplace=True)
        calc_obj.get_statistics(final)
        return st.dataframe(final, use_container_width=True)