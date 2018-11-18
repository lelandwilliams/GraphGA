from math import cos, asin, sqrt
from collections import OrderedDict

def distance_from_ll(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

def getDistances(cities):
    # Given a cities dictionary
    # returns M, a matrix of distances between cities
    c_names = list(cities.keys())
    M = OrderedDict()
    for i in range(len(c_names)):
        M[c_names[i]] = {}
    for i in range(len(c_names) -1 ):
        lat1, lon1 = cities[c_names[i]]
#       print(lat1, ',',  lon1)
        for j in range(i+1, len(c_names)):
            lat2, lon2 = cities[c_names[j]]
            dist = distance_from_ll(lat1, lon1, lat2, lon2)
            M[c_names[i]][c_names[j]] = round(dist, 2)
            M[c_names[j]][c_names[i]] = round(dist, 2)
        
    #M[c_names[-1] = {} # give last city an empty dictionary
    return M

def getCities(fname, n = -2):
    # since we use n+1 as limit, 
    # default will be n = -1
    f = open(fname, "r")
    lines = f.readlines()[1:n+1]
    cities = OrderedDict()
    for l in lines:
        items = l.split()
        #print(len(items))
        cities[items[1]] = (float(items[3]), float(items[4]))

    f.close()
    return cities

    

