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
        with st.expander('Expand to preview the data.'):
            st.write(st.session_state.traffic_df.head())
        ############ search part
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
            self.on_search(search_target, search_keyword)

        ############ sort part
        st.markdown("### SORT")
        sort_spaces1, sort_spaces2, sort_spaces3 = st.columns(3)

        sort_target = sort_spaces1.selectbox(
            "Sort a record", st.session_state.traffic_df.columns, key = "<aaa>")

        sort_way = sort_spaces2.selectbox(
            "Ascending order or not", ['ascending', 'non-ascending'])

        sort_display_num = sort_spaces3.text_input(
            "Max. number of items", placeholder="default: 10")

        is_sort = sort_spaces1.button("Sort 🔍")

        if is_sort:
            self.on_sort(sort_target, sort_way, sort_display_num)

        return 
    
    @capture_time
    def on_search(self, search_target, search_keyword):
        st.subheader("📋 Search results:")
        start_time = time.time()
        if search_keyword == '':
            result = 'please enter a keyword'
        else:
            # TODO: highlight the search results
            result = self.data_handler.search(st.session_state.traffic_df, search_target, search_keyword)
        st.write(result)

    @capture_time
    def on_sort(self, sort_target, sort_way, sort_display_num):
        st.subheader("Sort results:")
        if sort_display_num == '':
            num = 10  # default is 10
        else:
            num = sort_display_num
            num = int(num)
        result = self.data_handler.sort(st.session_state.traffic_df, sort_target, sort_way, num)
        st.write(result)