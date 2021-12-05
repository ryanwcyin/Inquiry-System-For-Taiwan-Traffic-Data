import streamlit as st
import os
from function import TrafficDataHandler
import time
from traffic_data import TrafficData

class View:
    def __init__(self) -> None:
        self.data_handler = TrafficDataHandler()
        # Get the data to state
        if 'traffic_df' not in st.session_state:
            with st.spinner(f'Fetching the dataset...'):
                st.session_state.traffic_df = self.fetch_data()
        
    def capture_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            st.caption(f"Search done in {end_time - start_time:.4f}s")
            return res
        return wrapper

    @st.cache
    def fetch_data(self, filepath=os.path.join('data', 'TDCS_M06A_20190830_080000.csv')):
            traffic_data = TrafficData.from_file(filepath)  # default data path
            return traffic_data.data
    
    def render(self):
        st.header('🚥Inquiry System For Taiwan Traffic Data🚦')
        ############ loading the data
        with st.expander('Expand to peek the data and columns description.'):
            self._display_data_description()
        
        ############ search part
        self._display_search()

        ############ sort part
        self._display_sort()

        return 
    
    @capture_time
    def on_search(self, search_target, search_keyword):
        if search_keyword == '':
            result = 'please enter a keyword'
        else:
            # TODO: highlight the search results
            result = self.data_handler.search(st.session_state.traffic_df, search_target, search_keyword)
        return result

    @capture_time
    def on_sort(self, sort_target, sort_way, sort_display_num):
        if sort_display_num == '':
            num = 10  # default is 10
        else:
            num = sort_display_num
            num = int(num)
        result = self.data_handler.sort(st.session_state.traffic_df, sort_target, sort_way, num)
        return result

    def display_results(self, name_of_result):
        result = st.session_state[name_of_result]
        if len(result) > 10 and not isinstance(result, str):
            max_page=len(result)//10+1
            part_to_show = st.slider('Pagination', min_value=1, max_value=max_page, format=f"Page %i of {max_page}")
            st.write(result.iloc[(part_to_show-1) * 10 : part_to_show * 10])
        elif isinstance(result, str):
            st.warning(result)
        else:
            st.write(result)

    def _display_data_description(self):
        st.markdown("#### First 5 rows of the dataset")
        st.write(st.session_state.traffic_df.head())
        st.markdown("""
        #### Column descriptions:
        |  Columns |  Descriptions |
        |---|---|
        | 'VehicleType' |  車種，31小客車、32小貨車、41大客車、42大貨車、5聯結車 |
        | 'DerectionTime_O' |  車輛通過本旅次第1個測站時間 |
        | 'GantryID_D' | 車輛通過本旅次第1個測站編號 |
        | 'DerectionTime_D' |  車輛通過本旅次最後1個測站時間 |
        | 'TripLength' | 本旅次行駛距離  |
        | 'TripEnd' | 旅次標記(Y正常結束，N異常)  |
        | 'TripInformation' |  本旅次經過各個測站之通過時間及編號 |
        
        """)
    
    def _display_search(self):
        st.markdown("### SEARCH")
        search_spaces1, search_spaces2 = st.columns([1, 1])

        search_target = search_spaces1.selectbox(
            "Search a record", st.session_state.traffic_df.columns)
        is_search = search_spaces1.button("Search 🔍", )
        if search_target in ['DerectionTime_O', 'DerectionTime_D']:
            search_keyword = search_spaces2.text_input(
                " ", placeholder="(YYYY-MM-DD HH:MM:SS)"
            )
        else:
            search_keyword = search_spaces2.text_input(
                "keyword", placeholder="Input your keyword"
            )

        if is_search:
            with st.spinner(f'Searching: {search_keyword} ...'):
                result = self.on_search(search_target, search_keyword)
                st.session_state.search_result = result
        if st.session_state.get('search_result') is not None:
            st.subheader("Search results:")
            self.display_results('search_result')

    def _display_sort(self):
        st.markdown("### SORT")
        sort_spaces1, sort_spaces2, sort_spaces3 = st.columns(3)

        sort_target = sort_spaces1.selectbox(
            "Sort a record", st.session_state.traffic_df.columns, key = "<aaa>")
        sort_way = sort_spaces2.selectbox(
            "Ascending order or not", ['ascending', 'descending'])
        sort_display_num = sort_spaces3.text_input(
            "Max. number of items", placeholder="default: 10")
        is_sort = sort_spaces1.button("Sort 🔍")

        if is_sort:
            result = self.on_sort(sort_target, sort_way, sort_display_num)
            st.session_state.sort_result = result
        if st.session_state.get('sort_result') is not None:
            st.subheader("Sort results:")
            self.display_results('sort_result')