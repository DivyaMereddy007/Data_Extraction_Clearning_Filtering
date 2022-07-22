#https://towardsdatascience.com/driving-distance-between-two-or-more-places-in-python-89779d691def

import pandas as pd
import requests # to get the distances from the API
import json # to read the API response
 # for travelling salesman problem
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import datetime

# load the dataframe with capitals
df = pd.read_csv("/Users/divyamereddy/Documents/GitHub/Data_Extraction_Clearning_Filtering/Distance_Problems_Gmaps_Based/Sales_Man_Travel_Problem/concap.csv")
df=df[1:100]
# rename so that the column names are shorter and comply with PEP-8
df.rename(columns={"CountryName": "Country", "CapitalName": "capital", "CapitalLatitude": "lat", "CapitalLongitude": "lon", "CountryCode": "code", "ContinentName": "continent"}, inplace=True)

# filter only the capitals of the Central Europe
ce_countries = ["AT","CZ","DE","HU","LI","PL","SK","SI","CH"]
ce_cities = df[df["code"].isin(ce_countries)].reset_index(drop=True)

def get_distance(point1: dict, point2: dict) -> tuple:
    """Gets distance between two points en route using http://project-osrm.org/docs/v5.10.0/api/#nearest-service"""

    url = f"""http://router.project-osrm.org/route/v1/driving/{point1["lon"]},{point1["lat"]};{point2["lon"]},{point2["lat"]}?overview=false&alternatives=false"""
    r = requests.get(url)

    # get the distance from the returned values
    route = json.loads(r.content)["routes"][0]
    return (route["distance"], route["duration"])

# get the distances and durations
dist_array = []
for i , r in ce_cities.iterrows():
    point1 = {"lat": r["lat"], "lon": r["lon"]}
    for j, o in ce_cities[ce_cities.index != i].iterrows():
        point2 = {"lat": o["lat"], "lon": o["lon"]}
        dist, duration = get_distance(point1, point2)
        #dist = geodesic((i_lat, i_lon), (o["CapitalLatitude"], o["CapitalLongitude"])).km
        dist_array.append((i, j, duration, dist))

dist_array

distances_df = pd.DataFrame(dist_array,columns=["origin","destination","duration(s)","distnace(m)"])
distances_df
# turn the first three columns of the dataframe into the list of tuples
dist_list = list(distances_df[["origin","destination","duration(s)"]].sort_values(by=["origin","destination"]).to_records(index=False))
dist_list[:5] + ["..."] + dist_list[-5:]


# we plan to use the list of distnaces (durations in our case), that's why we initialize with `distances = dist_list` param.
fitness_dists = mlrose.TravellingSales(distances = dist_array)

# we plan to visit 9 cities
length = ce_cities.shape[0]

problem_fit = mlrose.TSPOpt(length = length, fitness_fn = fitness_dists,
                            maximize=False)

# non-ideal solution, without specifying mlrose optimization
mlrose.genetic_alg(problem_fit, random_state = 2)

# better but more resource intensive solutions
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,  max_attempts = 500, random_state = 2)


print(f"The best state found is: {best_state}, taking {best_fitness} ({str(datetime.timedelta(seconds=best_fitness))})")
#The best state found is: [1 8 4 7 3 6 0 5 2], taking 157397.0 (1 day, 19:43:17)

# turn the results to an ordered dict
orders = {city: order for order, city in enumerate(best_state)}
orders

# apply this order to the dataframe with the cities
ce_cities["order"] = ce_cities.index.map(orders)
ce_cities = ce_cities.sort_values(by="order")
ce_cities
