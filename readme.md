# Inquiry system for Taiwan traffic 🚦

### Installation:
```
pip install -r requirements.txt
```

### Start local app:
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


### TODO ✅:
- [ ] Search
- [ ] Sort
- [ ] Join


### Acknowledgement: 
Column descriptions are available at:
https://web.archive.org/web/20191103004550/http://tisvcloud.freeway.gov.tw/TISVCloud_web.files/TDCS_M06A.htm