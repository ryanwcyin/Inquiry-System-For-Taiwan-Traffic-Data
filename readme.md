# Inquiry system for Taiwan traffic ð¦

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
| 'VehicleType' |  è»ç¨®ï¼31å°å®¢è»ã32å°è²¨è»ã41å¤§å®¢è»ã42å¤§è²¨è»ã5è¯çµè» |
| 'DerectionTime_O' |  è»è¼ééæ¬ææ¬¡ç¬¬1åæ¸¬ç«æé |
| 'GantryID_D' | è»è¼ééæ¬ææ¬¡ç¬¬1åæ¸¬ç«ç·¨è |
| 'DerectionTime_D' |  è»è¼ééæ¬ææ¬¡æå¾1åæ¸¬ç«æé |
| 'TripLength' | æ¬ææ¬¡è¡é§è·é¢  |
| 'TripEnd' | ææ¬¡æ¨è¨(Yæ­£å¸¸çµæï¼Nç°å¸¸)  |
| 'TripInformation' |  æ¬ææ¬¡ç¶éååæ¸¬ç«ä¹ééæéåç·¨è |


### Update info. ð 

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


### TODO â:
- highlight the keywords
- add range search
- visualize sorting(searching) time


### Acknowledgement: 
Column descriptions are available at:
https://web.archive.org/web/20191103004550/http://tisvcloud.freeway.gov.tw/TISVCloud_web.files/TDCS_M06A.htm