import math
#*Calculate difference between two points using latitude and longitude
#*we shall use haversine formula

def find_difference_using_lat_long(lat1 , lon1 , lat2 , lon2):
    '''Accepts and latitudes and longitudes of two points in degrees . Returns the differnce between them using haversine formula'''
    lat1_radians = math.radians(lat1)
    lat2_radians = math.radians(lat2)
    lon1_radians = math.radians(lon1)
    lon2_radians = math.radians(lon1)

    latitude_diff = lat1_radians - lat2_radians
    longitude_diff = lon1_radians - long2_radians

    a = (math.sin(latitude_diff/2)**2) + math.cos(lat1_radians)*math.cos(lat2_radians)*(math.sin(longitude_diff/2)**2)
    c = 2 *math.atan2(math.sqrt(a) , math.sqrt(1-a))
    d = 6371 * c 

    return d

find_difference_using_lat_long()