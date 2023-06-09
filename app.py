import pandas as pd
import datetime as dt
import requests
import numpy as np
from pandas import json_normalize
import datetime
import streamlit as st
from datetime import date


from loader import GetDataFromAPI
loader_obj = GetDataFromAPI()
from calculate import Calculate
calc_obj =  Calculate()
from plotter import Plot
plotter_obj = Plot()



st.set_page_config(layout='wide', page_title='SiesmoStream')


# st.slider('hello')
# hitting the API and storing result in response variable
# response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-04-29&endtime=2023-04-30&minmagnitude=5')

today = dt.date.today()
week_ago = today - dt.timedelta(days=7)
yesterday = today - dt.timedelta(days=1)
first_day_month = today.replace(day=1)
year = date(date.today().year, 1, 1)



st.sidebar.header('SiesmoStream')
option = st.sidebar.radio('Select', ['About','QuakeView', 'QuakeEdu'])

# choosing what to do based on selected radio buttons
if option == 'QuakeView':
    st.sidebar.markdown('*Earthquake visualization on an interactive map*')
    st.header('QuakeView')
    st.markdown('---')
    # final = loader_obj.load_clean_data(response)

    city_date_option = st.sidebar.selectbox('Visualize On', ['Date', 'City/State'])
    if city_date_option == 'Date':
        date_option = st.sidebar.selectbox('Choose Dates', ['Today', 'This Week', 'This Month', 'This Year', 'Custom Date Range'])

        if date_option == 'Today':
            # btn = st.sidebar.button('Visualize')
            # if btn == True:
            response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(yesterday, today))
            final = loader_obj.load_clean_data(response)
            calc_obj.get_statistics(final)
            # st.dataframe(final, use_container_width=True)
            st.subheader('Interactive Map')
            map_option = st.selectbox('Choose Map Style', ['Terrain', 'Light', 'Dark'])
            if map_option == 'Terrain':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Light':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Dark':
                plotter_obj.plot_iteractive_map(final, map_option)
            st.markdown('---')
            histogram_option = st.selectbox('Choose Histogram Style', ['Normal', 'Stacked'])
            if histogram_option == 'Normal':
                plotter_obj.plot_histogram(final, histogram_option)
            if histogram_option == 'Stacked':
                plotter_obj.plot_histogram(final, histogram_option)


        # String format used to put today's date and a date from week ago as params to the API
        if date_option == 'This Week':

            # btn = st.sidebar.button('Visualize', key='button')
            # if st.session_state['button'] == btn:
            response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(week_ago, today))
            final = loader_obj.load_clean_data(response)
            calc_obj.get_statistics(final)
            mag_slider = st.slider('Filer by magnitude', min_value= float(final['mag'].min()), max_value=float(final['mag'].max()))
            final = final[final['mag'] > mag_slider]
            # st.dataframe(final, use_container_width=True)
            # st.dataframe(final, use_container_width=True)
            st.subheader('Interactive Map')
            map_option = st.selectbox('Choose Map Style', ['Terrain', 'Light', 'Dark'])
            if map_option == 'Terrain':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Light':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Dark':
                plotter_obj.plot_iteractive_map(final, map_option)
            st.markdown('---')
            histogram_option = st.selectbox('Choose Histogram Style', ['Normal', 'Stacked'])
            if histogram_option == 'Normal':
                plotter_obj.plot_histogram(final, histogram_option)
            if histogram_option == 'Stacked':
                plotter_obj.plot_histogram(final, histogram_option)
        

        if date_option == 'This Month':
            # btn = st.sidebar.button('Visualize', key='button')
            # if st.session_state['button'] == btn:
            try:
                response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(first_day_month, today))
                final = loader_obj.load_clean_data(response)
                calc_obj.get_statistics(final)
                mag_slider = st.slider('Filer by magnitude', min_value= float(final['mag'].min()), max_value= float(final['mag'].max()))
                final = final[final['mag'] > mag_slider]
                # st.dataframe(final, use_container_width=True)
            except:
                st.warning('Please select the option labeled \'Today\' as it is the first day of the month.')
            st.subheader('Interactive Map')
            map_option = st.selectbox('Choose Map Style', ['Terrain', 'Light', 'Dark'])
            if map_option == 'Terrain':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Light':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Dark':
                plotter_obj.plot_iteractive_map(final, map_option)
            st.markdown('---')
            histogram_option = st.selectbox('Choose Histogram Style', ['Normal', 'Stacked'])
            if histogram_option == 'Normal':
                plotter_obj.plot_histogram(final, histogram_option)
            if histogram_option == 'Stacked':
                plotter_obj.plot_histogram(final, histogram_option)


        if date_option == 'This Year':
            # btn = st.sidebar.button('Visualize', key='button')
            # if st.session_state['button'] == btn:
            response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(year, today))
            final = loader_obj.load_clean_data(response)
            calc_obj.get_statistics(final)
            mag_slider = st.slider('Filer by magnitude', min_value= float(final['mag'].min()), max_value= float(final['mag'].max()))
            final = final[final['mag'] > mag_slider]
            # st.dataframe(final, use_container_width=True)
            st.subheader('Interactive Map')
            map_option = st.selectbox('Choose Map Style', ['Terrain', 'Light', 'Dark'])
            if map_option == 'Terrain':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Light':
                plotter_obj.plot_iteractive_map(final, map_option)
            if map_option == 'Dark':
                plotter_obj.plot_iteractive_map(final, map_option)
            st.markdown('---')
            histogram_option = st.selectbox('Choose Histogram Style', ['Normal', 'Stacked'])
            if histogram_option == 'Normal':
                plotter_obj.plot_histogram(final, histogram_option)
            if histogram_option == 'Stacked':
                plotter_obj.plot_histogram(final, histogram_option)


        if date_option == 'Custom Date Range':
        #     btn = st.sidebar.button('Visualize', key='button')
            st.sidebar.markdown("<p style='color: orange;'>Note: If you select a wide range of dates that span several years, the data may not be displayed.</p>", unsafe_allow_html=True)
            start_date = st.date_input('Choose Start Date', max_value=today)
            end_date = st.date_input('Choose End Date', min_value=start_date, max_value=today)
            if end_date <= start_date:
                st.warning('Please choose an end date after the start date.')

            # if st.session_state['button'] == btn:   
            try: 
                response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}&minmagnitude=5'.format(start_date, end_date))
                final = loader_obj.load_clean_data(response)
                calc_obj.get_statistics(final)
                mag_slider = st.slider('Filer by magnitude', min_value= float(final['mag'].min()), max_value= float(final['mag'].max()))
                final = final[final['mag'] > mag_slider]
                # st.dataframe(final, use_container_width=True)
                st.subheader('Interactive Map')
                map_option = st.selectbox('Choose Map Style', ['Terrain', 'Light', 'Dark'])
                if map_option == 'Terrain':
                    plotter_obj.plot_iteractive_map(final, map_option)
                if map_option == 'Light':
                    plotter_obj.plot_iteractive_map(final, map_option)
                if map_option == 'Dark':
                    plotter_obj.plot_iteractive_map(final, map_option)
                st.markdown('---')
                histogram_option = st.selectbox('Choose Histogram Style', ['Normal', 'Stacked'])
                if histogram_option == 'Normal':
                    plotter_obj.plot_histogram(final, histogram_option)
                if histogram_option == 'Stacked':
                    plotter_obj.plot_histogram(final, histogram_option)
            except:
                st.error('Data for the selected date range isn\'t available.')
    


    if city_date_option == 'City/State':
        response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=1-1-2015&endtime={}&minmagnitude=5'.format(today))
        final = loader_obj.load_clean_data(response)
        chosen_country = st.sidebar.selectbox('Choose the City/Country', sorted(list(final['city/state'].dropna().unique())))
        plotter_obj.plot_country(final, chosen_country)
            



if option == 'QuakeEdu':
    st.sidebar.markdown('*Learn earthquake preparedness tips and science behind seismic events*')
    st.header('QuakeEdu')
    st.write('Here, we\'ll delve into the fascinating world of earthquakes and explore the forces that shape our planet. Get ready to uncover the basics of earthquakes, from their origins to the intricate geological processes at play.')

    st.write('In this section, we\'ll demystify earthquakes by explaining what they are and how they occur. We\'ll take a closer look at the remarkable concept of plate tectonics, which underlies the movement and interactions of Earth\'s crustal plates. Discover how these dynamic plates can collide, slide past each other, or separate, triggering seismic activity along fault lines.')
    st.markdown('---')

    st.subheader('Basics of Earthquake')
    st.write('- An earthquake is a shaking or trembling of the Earth\'s surface caused by the sudden release of energy in the Earth\'s crust.')
    st.write('- The movement of tectonic plates, which are large sections of the Earth\'s crust, is responsible for earthquakes.')
    st.write('- Most earthquakes occur along fault lines, which are fractures or cracks in the Earth\'s crust where significant plate movement takes place.')
    st.write('- When stress along a fault line becomes too great, the rocks suddenly slip, releasing stored energy and causing seismic waves.')
    st.write('- The severity or magnitude of an earthquake is measured using the Richter scale or similar scales, which quantify the energy released.')
    st.write('- Scientists use instruments like seismographs to monitor and analyze earthquakes, improving our understanding of their patterns and impacts.')
    

    # https://stackoverflow.com/questions/70932538/how-to-center-the-title-and-an-image-in-streamlit    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')
    with col2:
        st.image("Media/Earthquake Process.jpg", width=300)
    with col3:
        st.write(' ')

    st.markdown('---')

    st.subheader('Effects of Earthquakes')
    st.write('- **Ground shaking:**  Earthquakes cause the ground to shake, leading to the collapse of buildings, infrastructure damage, and the potential for injuries or fatalities.')
    st.write('- **Surface rupture:** Some earthquakes can cause visible cracks or displacement along the Earth\'s surface, damaging roads, pipelines, and structures in the affected area.')
    st.write('- **Landslides:** The intense shaking during an earthquake can trigger landslides, resulting in the collapse of slopes and the potential for burying communities and infrastructure.')
    st.write('- **Tsunamis:** Underwater earthquakes can generate tsunamis, which are powerful ocean waves that can devastate coastal areas, causing widespread flooding and destruction.')
    st.write('- **Structural damage:** Buildings and infrastructure can suffer significant damage during earthquakes, compromising their integrity and leading to collapses or unsafe conditions.')

    col1, col2 = st.columns(2)

    with col1:
        st.image("Media/Landslide.jpg")
    with col2:
        st.image("Media/road damage.jpg", width=300)
    # with col3:
    #     st.image("Media/structural damage.jpg")

    st.markdown('---')

    st.subheader('Earthquake Safety')
    st.write('- **Secure furniture and heavy objects:** Use brackets, straps, or anchors to secure heavy furniture, appliances, and other objects to prevent them from falling or causing injuries during an earthquake.')
    st.write('- **Identify safe spots:** Identify safe spots in your home or workplace, such as under sturdy tables or desks, and teach everyone in your household or office to "Drop, Cover, and Hold On" during an earthquake.')
    st.write('- **Stay away from hazards:** Keep away from windows, glass, mirrors, and other objects that could shatter during an earthquake. Stay clear of heavy furniture or fixtures that could topple over.')
    st.write('- **Stay informed:** Follow official sources of information, such as local authorities and emergency management agencies, for updates on earthquake warnings, alerts, and safety instructions.')
    st.write('- **Check for gas and electrical hazards:** After an earthquake, check for gas leaks, electrical damage, and potential hazards like broken wires. If you suspect a gas leak, turn off the main gas valve and immediately leave the area.')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')
    with col2:
        st.image("Media/Earthquake Safety.jpg", width=200)
    with col3:
        st.write(' ')


if option == 'About':
    st.header('SiesmoStream')
    st.markdown('*SeismoStream: Because earthquakes aren\'t just for the birds.*')
    st.markdown('---')
    st.sidebar.markdown('*Learn more about the project*')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGI0ZWU5ZDcyM2FhOGE3NzVjZmQ2MzIxNzM3NGEyMmNlNmMyYWZjNSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/TdXeFkgX9nHqsZWkX0/giphy.gif)")

    with col2:
        for i in range(0, 20):
            st.write(' ')
        st.markdown("![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGI0ZDVjNzIyNDU0NzJlMWJmMGE2MzU3MDZiZmIwY2U3MjE0N2QwNyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/KuDCWZNEjzLqdlUKk0/giphy.gif)")
    
    # st.video('Landing_video.gif')

    st.subheader('Introduction')
    st.write('Welcome to my earthquake plotting app! If you\'re anything like me, you\'re probably fascinated by the powerful forces of nature that can shake the ground beneath our feet. That\'s why I created this app - to help you explore and visualize earthquake data in a fun and interactive way!')
    st.write('With my app, you can easily plot earthquake data on a map and explore patterns and trends over time. Whether you\'re a seasoned geologist or just a curious beginner, this app is perfect for anyone who wants to learn more about earthquakes and their impact on the world.')
    st.write('So go ahead and give it a try! You might just discover something new and exciting about this amazing planet we call home.')
    st.markdown('---')

    st.subheader('Unveiling the Spectacular Features!')
    st.write('Hey there! So, in my app, you\'ll find some really cool visualizations that will help you explore earthquake data like never before!')
    st.write('- I\'ve created interactive maps that allow you to explore earthquakes by location. You can zoom in or out and click on any point to see the details of the earthquake that occurred at that location.')
    st.write('- But that\'s not all! I\'ve also created animations that show you how earthquakes have occurred over time. These animations give you a great perspective on how earthquakes have evolved over a specific period.')
    st.write('- I\'ve also included bar charts and line charts that show you how the frequency and magnitude of earthquakes have changed over time. This can help you identify patterns and trends in the occurrence of earthquakes.')

    st.markdown('---')
    st.subheader('How to use?')
    st.write('- Choose to visualize on date or on country')
    st.write('###### For Date')
    st.write("- You can select from various time ranges such as today, this week, this month, or this year. Alternatively, you can provide a custom date to explore earthquake data.")
    st.write("- The graph will automatically update once you choose the date or time range.")
    st.write("- To view the Year On Year Statistics, simply click on the button. This will display visually appealing statistics for the last 10 years.")

    st.write('###### For Country')
    st.write("- Select a country from the dropdown menu.")
    st.write("- Once you choose a country, you will see the country statistics along with the plotted historical earthquake data.")
    st.markdown('---')

    st.subheader("Credits:")
    st.write("- Earthquake data provided by the USGS API (https://earthquake.usgs.gov/fdsnws/event/1/)")
    st.write("- Geocoding data provided by the OpenCage Data API (https://opencagedata.com/api)")
    st.markdown('---')
    
    st.subheader('Connect with me:')
    st.markdown('<p align="left"><a href="https://www.linkedin.com/in/aditya-ramachandran-27b2ab24a/" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/-LinkedIn-0077B5?logo=linkedin&logoColor=white&style=for-the-badge" alt="LinkedIn" /></a></p>', unsafe_allow_html=True)
    st.markdown('<p align="left"><a href="https://github.com/Aditya-Ramachandran" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white&style=for-the-badge" alt="GitHub" /></a></p>', unsafe_allow_html=True)
    st.markdown('---')



    # https://stackoverflow.com/questions/70680012/play-muted-loop-video-on-streamlit

    # col1, col2 = st.columns([1, 1])

    # video_html = """
    #             <video controls width="500" autoplay="true" muted="true" loop="true">
    #             <source src="https://www.youtube.com/watch?v=qoN3oKO91Ak&list=RDMMJAIVxKw36Rg&index=23" type="video/mp4">
    #             </video>
    #             """
    # col2.markdown(video_html, unsafe_allow_html=True)