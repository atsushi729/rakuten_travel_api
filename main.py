import json

import requests
import pandas as pd

REQUEST_URL = ''
APP_ID = ''

params = {
    'format': 'json',
    'largeClassCode': 'japan',
    'middleClassCode': 'okinawa',
    'smallClassCode': 'nahashi',
    'applicationId': APP_ID
}

res = requests.get(REQUEST_URL, params)
result = res.json()

df = pd.DataFrame()
hotels = result['hotels']

for i, hotel in enumerate(hotels):
    hotel_info = hotel['hotel'][0]['hotelBasicInfo']
    temp = pd.DataFrame(hotel_info, index=[i])
    df = df.append(temp)

df[[
    'hotelNo', 'hotelName', 'hotelInformationUrl',
    'hotelImageUrl', 'reviewCount', 'reviewAverage'
]].to_csv('hotel.csv', index=False)
