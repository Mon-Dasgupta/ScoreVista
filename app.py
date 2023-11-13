import streamlit as st
import pickle
import pandas as pd

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
        background-color: #317773;
        color: #333;
        font-family: 'Arial', sans-serif;

    }

    .stApp {
        max-width: 800px;
        margin: 0 auto;
        max-width: 800px;
        background-color:#E2D1F9
    }
    .stTitle {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #004080;
        font-family: 'Edu TAS Beginner SemiBold', cursive;
        background-color:#D6DEDC;
        overflow: hidden;
        border-right: .15em solid orange;
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: .15em;
        animation: typing 2s steps(100) 3;

    }
    .stButton {
        padding: 10px 20px;
        border-radius:5px;
        background-color:#8bb1d6  !important;  
        color: #361313 !important;
        font-weight: bold !important;
        font-size: 16px !important;
        font-family: 'Edu TAS Beginner SemiBold', cursive;

    }
    .stSelectbox {
        background-color:#e6d1d1 !important;
        color: #333 !important;
    }
    .stNumberInput {
        background-color: #e6d1d1 !important;
        color: #333 !important;
    }
    .stTextInput {
        background-color: #e6d1d1 !important;
        color: #333 !important;
    }

    @keyframes typing {
        from {
            width: 0;
        }
        to {
            width: 100%;
        }
    }


"""

# Apply custom CSS
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# Page title
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

# Logo image
# from PIL import Image
#
# image = Image.open('pitch.jpg')
#
# st.image(image,width=350,output_format="PNG");


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

