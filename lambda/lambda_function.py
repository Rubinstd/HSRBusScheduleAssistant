from google.transit import gtfs_realtime_pb2
from urllib.request import urlopen
import csv
from datetime import datetime
import pandas as pd

def getGTFS(routeName):
    
    arrivalTimes = []
    # Setup GTFS feed.
    feed = gtfs_realtime_pb2.FeedMessage()
    response = urlopen('http://opendata.hamilton.ca/GTFS-RT/GTFS_TripUpdates.pb')
    feed.ParseFromString(response.read())

    routeIds, tripIds = getIdsFromRouteName(routeName)

    onRoute = [entity for entity in feed.entity if int(entity.trip_update.trip.route_id) in routeIds]
    relevantTrips = [entity for entity in onRoute if int(entity.trip_update.trip.trip_id) in tripIds]

    for trip in relevantTrips:
        nearestStopData = [ stopUpdate for stopUpdate in trip.trip_update.stop_time_update if int(stopUpdate.stop_id) == 355742]
        arrivalTimes += [ datetime.fromtimestamp(update.arrival.time) for update in nearestStopData ]
    
    return arrivalTimes
            

def getIdsFromRouteName(routeName):
    data = pd.read_csv("./data/trips.txt") 
    filteredTrips = data[data['trip_headsign'].str.contains(routeName)]

    routeIds = filteredTrips['route_id'].unique()
    tripIds = filteredTrips['trip_id'].unique()

    return routeIds, tripIds
    

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }




###### SCRAP CODE #######
#    for entity in onRoute:
        #print(entity.trip_update.stop_time_update)
#        for stop_time_update in entity.trip_update.stop_time_update:
#            if int(stop_time_update.stop_id) == 355742:
#                ts = int(stop_time_update.arrival.time)
#                print(datetime.fromtimestamp(ts))
        #break
        #if entity.HasField('trip_update'):
        #    print(entity.trip_update)
