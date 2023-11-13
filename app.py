# import  streamlit as st
# import pickle
# import pandas as pd
# import numpy as np
#
# #pipe = pickle.load(open('pipe.pkl','rb'))
#
# with open('pipe.pkl', 'rb') as file:
#  loaded_pipeline = pickle.load(file)
#
# teams = ['Australia',
#  'India',
#  'Bangladesh',
#  'New Zealand',
#  'South Africa',
#  'England',
#  'West Indies',
#  'Afghanistan',
#  'Pakistan',
#  'Sri Lanka']
#
# cities =['Colombo',
#  'Mirpur',
#  'Johannesburg',
#  'Melbourne',
#  'Dubai',
#  'Sydney',
#  'St Lucia',
#  'Auckland',
#  'Cape Town',
#  'London',
#  'Sylhet',
#  'Barbados',
#  'Pallekele',
#  'Wellington',
#  'Mumbai',
#  'Hamilton',
#  'Durban',
#  'Kuala Lumpur',
#  'Galle',
#  'Delhi',
#  'Canberra',
#  'Centurion',
#  'Lauderhill',
#  'Mount Maunganui',
#  'Southampton',
#  'Sharjah',
#  'Manchester',
#  'Nottingham',
#  'Karachi',
#  'Guyana',
#  'Bangalore',
#  'Abu Dhabi',
#  'Brisbane',
#  'Potchefstroom',
#  'Trinidad',
#  'Nagpur',
#  'Kolkata',
#  'Lahore',
#  'Chittagong',
#  'Perth',
#  'Bristol',
#  'Cardiff',
#  'Chelmsford',
#  'Chandigarh',
#  'Adelaide',
#  'Antigua',
#  'Taunton',
#  'Birmingham',
#  'Derby',
#  'Kandy',
#  'Chennai',
#  'Christchurch',
#  'Chester-le-Street']
#
# st.title('Cricket Score Predictor')
#
# col1,col2 = st.columns(2)
#
# with col1:
#     batting_team=st.selectbox('Select batting team',sorted(teams))
# with col2:
#     bowling_team = st.selectbox('Select bowling team', sorted(teams))
#
# city = st.selectbox('Select city',sorted(cities))
#
# col3,col4,col5 = st.columns(3)
#
# with col3:
#     current_score = st.number_input('Current Score')
#
# with col4:
#     overs = st.number_input('Overs Done(works for overs>5')
#
# with col5:
#     wickets = st.number_input('Wickets out')
#
# last_five = st.number_input('Runs scorerd in last five overs')
#
# if st.button('Predict Score'):
#     balls_left = 120 - (overs*6)
#     wickets_left = 10 - wickets
#     crr = current_score/overs
#
#     input_df = pd.DataFrame(
#      {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': city, 'current_score': [current_score],
#       'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five]})
#
#     result = loaded_pipeline.predict(input_df)
#     st.header("Predicted Score - " + str(int(result[0])))

    # Additional styling for the result
    # st.markdown(
    #  """
    #  <style>
    #      .css-1aumxhk {
    #          background-color: #f0f0f0; /* Change background color */
    #          padding: 10px;
    #          border-radius: 5px;
    #      }
    #  </style>
    #  """,
    #  unsafe_allow_html=True
    # )


import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
with open('pipe.pkl', 'rb') as file:
    loaded_pipeline = pickle.load(file)

teams = ['Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 'England', 'West Indies', 'Afghanistan',
         'Pakistan', 'Sri Lanka']

cities = ['Colombo', 'Mirpur', 'Johannesburg', 'Melbourne', 'Dubai', 'Sydney', 'St Lucia', 'Auckland', 'Cape Town',
          'London', 'Sylhet', 'Barbados', 'Pallekele', 'Wellington', 'Mumbai', 'Hamilton', 'Durban', 'Kuala Lumpur',
          'Galle', 'Delhi', 'Canberra', 'Centurion', 'Lauderhill', 'Mount Maunganui', 'Southampton', 'Sharjah',
          'Manchester', 'Nottingham', 'Karachi', 'Guyana', 'Bangalore', 'Abu Dhabi', 'Brisbane', 'Potchefstroom',
          'Trinidad', 'Nagpur', 'Kolkata', 'Lahore', 'Chittagong', 'Perth', 'Bristol', 'Cardiff', 'Chelmsford',
          'Chandigarh', 'Adelaide', 'Antigua', 'Taunton', 'Birmingham', 'Derby', 'Kandy', 'Chennai', 'Christchurch',
          'Chester-le-Street']

# Custom CSS for styling
custom_css = """
    body {
        background-color: #F7F7F7;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .stTitle {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #004080;
    }
    .stButton {
        background-color: #004080 !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }
    .stSelectbox {
        background-color: #E0E0E0 !important;
        color: #333 !important;
    }
    .stNumberInput {
        background-color: #E0E0E0 !important;
        color: #333 !important;
    }
    .stTextInput {
        background-color: #E0E0E0 !important;
        color: #333 !important;
    }
"""

# Apply custom CSS
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# Page title
st.title('Cricket Score Predictor')
st.markdown('<p class="stTitle">Cricket Score Predictor</p>', unsafe_allow_html=True)

# Columns layout
col1, col2 = st.columns(2)

# Select batting team
with col1:
    batting_team = st.selectbox('Select batting team', sorted(teams), key='batting_team')

# Select bowling team
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams), key='bowling_team')

# Select city
city = st.selectbox('Select city', sorted(cities), key='city')

# Input fields layout
col3, col4, col5 = st.columns(3)

# Current Score
with col3:
    current_score = st.number_input('Current Score', key='current_score')

# Overs
with col4:
    overs = st.number_input('Overs Done (works for overs > 5)', key='overs')

# Wickets
with col5:
    wickets = st.number_input('Wickets out', key='wickets')

# Last five overs
last_five = st.number_input('Runs scored in last five overs', key='last_five')

# Predict Score button
if st.button('Predict Score', key='predict-button', help="Click to predict the score"):
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = current_score / overs

    input_df = pd.DataFrame(
        {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': city, 'current_score': [current_score],
         'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five]})

    # Replace the next line with your actual prediction logic
    result = loaded_pipeline.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))



