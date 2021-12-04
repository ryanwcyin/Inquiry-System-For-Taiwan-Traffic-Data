import streamlit as st
import pandas as pd
import function as fc
import numpy as np

st.header('🚥Inquiry System For Taiwan Traffic Data🚦')

# default data path


@st.cache
def read_default_dataset(filepath=r'project2\Inquiry-System-For-Taiwan-Traffic-Data-master\data\TDCS_M06A_20190830_080000.csv'):
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

############ search part
st.markdown("### SEARCH")

search_spaces1, search_spaces2 = st.columns([1, 1])

search_target = search_spaces1.selectbox(
    "Search a record", traffic_df.columns)

is_search = search_spaces1.button("Search 🔍")

if search_target in ['DerectionTime_O', 'DerectionTime_D']:
    search_keyword = search_spaces2.text_input(
        " ", placeholder="(YYYY-MM-DD HH:MM:SS)"
    )
else:
    search_keyword = search_spaces2.text_input(
        "keyword", placeholder="Input your keyword"
    )

if is_search:
    st.subheader("Search result:")
    if search_keyword == '':
        result = 'please enter a keyword'
    else:
        result = fc.search(traffic_df, search_target, search_keyword)
        # df.style.applymap(lambda x: 'background-color : yellow' if x==a else '')
        # st.dataframe(result)
    st.write(result)
    # st.text('Loading~~~')

############ sort part
st.markdown("### SORT")
sort_spaces1, sort_spaces2, sort_spaces3 = st.columns(3)

sort_target = sort_spaces1.selectbox(
    "Sort a record", traffic_df.columns, key = "<aaa>")

sort_way = sort_spaces2.selectbox(
    "Ascending order or not", ['ascending', 'non-ascending'])

sort_displayNum = sort_spaces3.text_input(
    "Max. number of items", placeholder="default: 10")

is_sort = sort_spaces1.button("Sort 🔍")

if is_sort:
    st.subheader("Sort result:")
    if sort_displayNum == '':
        num = 10  # 默认返回10条信息
    else:
        num = sort_displayNum
        # print(type(num))
        num = int(num)
    result = fc.sort(traffic_df, sort_target, sort_way, num)
    st.write(result)

# st.file_uploader("Upload your own file to append to the dataframe:")

# st.subheader("Preview your data 📋")

# st.write(traffic_df.head())

