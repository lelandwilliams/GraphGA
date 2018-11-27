from math import cos, asin, sqrt
from collections import OrderedDict

def distance_from_ll(lat1, lon1, lat2, lon2):
    """ calculates the earth distance in km between the two coordinates """
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return round(12742 * asin(sqrt(a)), 2)

def getDistances(cities):
    """ returns a weighted matrix of of distances between cities,
    created from a dictionary of name->(lat, long) pairs """
    c_names = list(cities.keys())
    M = OrderedDict()
    for city1 in c_names:
        d = OrderedDict()
        for city2 in c_names:
            d[city2] = 0
        M[city1] = d

    idx = 1
    for city1 in c_names[:-1]:
        lat1, lon1 = cities[city1]
#       print(lat1, ',',  lon1)
        for city2 in c_names[idx:]:
            lat2, lon2 = cities[city2]
            dist = distance_from_ll(lat1, lon1, lat2, lon2)
            M[city1][city2] = round(dist, 2)
            M[city2][city1] = round(dist, 2)
        idx += 1
        
    #M[c_names[-1] = {} # give last city an empty dictionary
    return M

def getCities(fname, n = None):
    """ returns a dicitonary of name->(lat, long) pairs """
    f = open(fname, "r")
    limit = n+1 # the first line is a header
    if limit is None:
        limit = -1
    lines = f.readlines()[1:limit]
    cities = OrderedDict()
    for l in lines:
        items = l.split()
        #print(len(items))
        cities[items[1]] = (float(items[3]), float(items[4]))

    f.close()
    return cities

    

