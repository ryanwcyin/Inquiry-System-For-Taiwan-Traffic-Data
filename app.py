import streamlit as st
import pandas as pd

st.header('🚥Inquiry System For Taiwan Traffic Data🚦')

# default data path


@st.cache
def read_default_dataset(filepath=r'./data/default.csv'):
    df = pd.read_csv(filepath, header=None)
    df.columns = ['VehicleType',
                  'DerectionTime_O',
                  'GantryID_O',
                  'DerectionTime_D',
                  'GantryID_D',
                  'TripLength',
                  'TripEnd',
                  'TripInformation']
    return df


traffic_df = read_default_dataset()

search_spaces, sort_spaces = st.columns([1, 1])
search_target = search_spaces.text_input(
    "Search a record", placeholder="🔍 What are you looking for?")
is_search = search_spaces.button("Search 🔍")
sort_target = sort_spaces.selectbox(
    "Pick a column to sort?", traffic_df.columns)
is_sort = sort_spaces.button("Sort 🪜")

st.file_uploader("Upload your own file to append to the dataframe:")

st.subheader("Preview your data 📋")
st.write(traffic_df.head())
