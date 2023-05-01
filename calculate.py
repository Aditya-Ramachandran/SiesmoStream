import streamlit as st



class Calculate:

    def __init__(self) -> None:
            pass;

    def get_statistics(self, dataframe):
        maximum = dataframe['mag'].max()
        most_prone_city = dataframe['city/state'].value_counts().head(1).index[0]
        least_prone_city = dataframe['city/state'].value_counts().tail(1).index[0]
        most_prone_place = dataframe['place'].value_counts().head(1).index[0]
        least_prone_place = dataframe['place'].value_counts().tail(1).index[0]
        # print(maximum, most_pront_city, least_prone_city, most_prone_place, least_prone_place)
        # print(dataframe['city/state'].value_counts().head(1).values[0])
        st.markdown('##### Some cool stats!')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric('Maximum on Richter scale:', maximum)
        with col2:
            st.metric('Most Prone Country: ', most_prone_city)
        with col3:
            st.metric('Least Prone Country:', least_prone_city)
        col4, col5 = st.columns(2)
        with col4:  
            st.metric('Most Prone Place:', most_prone_place)
        with col5:
            st.metric('Least Prone Place:', least_prone_place)
        st.markdown("<p style='text-align: center;'><i>Scroll down for bar charts</i></p>", unsafe_allow_html=True)
        st.markdown('---')
