# Inquiry system for Taiwan traffic 🚦

### Quickstart:

Install the dependancies
```
pip install -r requirements.txt
```

Start the local app:
```
streamlit run app.py
```

### Column descriptions:
|  Columns |  Descriptions |
|---|---|
| 'VehicleType' |  車種，31小客車、32小貨車、41大客車、42大貨車、5聯結車 |
| 'DerectionTime_O' |  車輛通過本旅次第1個測站時間 |
| 'GantryID_D' | 車輛通過本旅次第1個測站編號 |
| 'DerectionTime_D' |  車輛通過本旅次最後1個測站時間 |
| 'TripLength' | 本旅次行駛距離  |
| 'TripEnd' | 旅次標記(Y正常結束，N異常)  |
| 'TripInformation' |  本旅次經過各個測站之通過時間及編號 |


### Update info. 📓 

- 04/12/2021
1. add search part
    user: 
    - choose a column
    - input a keyword

    return:
    - a dataframe contains the keyword

2. add sort part
    user:
    - choose a column
    - choose acsending or non-acsending
    - input the maximum display number of items

    return:
    - a dataframe which has been sorted


### TODO ✅:
- highlight the keywords
- add range search
- visualize sorting(searching) time


### Acknowledgement: 
Column descriptions are available at:
https://web.archive.org/web/20191103004550/http://tisvcloud.freeway.gov.tw/TISVCloud_web.files/TDCS_M06A.htm