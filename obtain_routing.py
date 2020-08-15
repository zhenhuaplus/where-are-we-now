# Extract routing info given coordinates using Mapbox API

import requests
import pandas as pd

def obtainRouting(starting_point, end_point):

    token = 'pk.eyJ1Ijoiemhlbmh1YSIsImEiOiJjazJjZnU2d2UwZHp6M2RvMmhhOGN6cG43In0.9F-J0PB0VUlBLxLE-TE_Tw'

    coordinates = str(starting_point[1]) + '%2C' \
                  + str(starting_point[0]) + '%3B' + str(end_point[1]) + '%2C' \
                  + str(end_point[0])

    # Obtain routing info
    link = 'https://api.mapbox.com/directions/v5/mapbox/driving/'
    response = requests.get(link + coordinates +
                            '?alternatives=true&geometries=geojson&steps=true&' +
                            'access_token=' + token)
    data = response.json()

    # Change routing list to dataframe
    # Input: [[-73.99604, 40.730953], [-73.998611, 40.732216], [-73.998611, 40.732216], ...]
    # Output: dataframe
    routing = data['routes'][0]['geometry']['coordinates']
    coord = pd.DataFrame()
    lat_list = []
    lon_list = []
    for i in range(len(routing)):
        lat_list.append(routing[i][1])
        lon_list.append(routing[i][0])
    coord['lat'] = lat_list
    coord['lon'] = lon_list

    return coord