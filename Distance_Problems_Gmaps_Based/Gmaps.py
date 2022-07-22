#https://medium.com/future-vision/google-maps-in-python-part-2-393f96196eaf
key='AIzaSyB4_i3OOyfHdKXPI1nIEl5nUihyUuqFSg4'

######################################

# Nessecary Imports
import matplotlib.pyplot as plt
import gmaps
gmaps.configure(api_key=key)
new_york_coordinates = (40.75, -74.00)
gmaps.figure(center=new_york_coordinates, zoom_level=12)

import gmaps
import gmaps.datasets
# Use google maps api
gmaps.configure(api_key=key) # Fill in with your API key
# Get the dataset
earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
#Get the locations from the data set
locations = earthquake_df[['latitude', 'longitude']]
#Get the magnitude from the data
weights = earthquake_df['magnitude']
#Set up your map
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
fig


#####################################################################################################################################################################

# importing required libraries
import requests, json
# Take source as input
source ='103 gale park ln,Nashville,TN'#input()
# Take destination as input
dest ='7521 Oakhaven Trace,Nashville,TN' #input()

# url variable store url
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'

url2="https://maps.googleapis.com/maps/api/distancematrix/json?origins=Seattle&destinations=San+Francisco&key=AIzaSyB4_i3OOyfHdKXPI1nIEl5nUihyUuqFSg4"
# Get method of requests module
# return response object
r = requests.get(url+'origins='+source+'&destinations='+dest+'&key='+ key)

# json method of response object
# return json format result
x = r.json()

# by default driving mode considered

# print the value of x
print(x['rows'][0]['elements'][0]['duration']['text'])

travel_time,distance=x['rows'][0]['elements'][0]['duration']['text'],x['rows'][0]['elements'][0]['distance']['text']
travel_time
travel_time=''
travel_time.split('mins')
travel_time,distance=x['rows'][0]['elements'][0]['duration']['text'],x['rows'][0]['elements'][0]['distance']['text']
travel_time
#travel_time=''
try:
    hours_time=int(travel_time.split('hours')[0])
    min_time=travel_time.split('hours')[1]
    min_time=int(min_time.split('min')[0])
except:
    hours_time=0
    min_time=int(travel_time.split('min')[0])
time=float(hours_time*60+min_time)
#####################################################################################################################################################################
sample_url_working='https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=AIzaSyB4_i3OOyfHdKXPI1nIEl5nUihyUuqFSg4'
# coordinations format
key='AIzaSyB4_i3OOyfHdKXPI1nIEl5nUihyUuqFSg4'
origin_coor = 8.866667,2.333333
destination_coor = 41.9, 12.48
# google API url
url = "https://maps.googleapis.com/maps/api/directions/json?origin={origin_coor}&destination={destination_coor}&mode=driving&key={key}"

r=requests.get(url)

results = json.loads(r.content)
legs = results.get("routes").pop(0).get("legs")
legs[0].get("duration"), legs[0].get("distance")


#####################################################################################################################################################################

import haversine as hs
loc1=(28.426846,77.088834)
loc2=(28.394231,77.050308)
hs.haversine(loc1,loc2)
