import GraphAlgorithms as galg
import maketable
import GA as ga

#cities = maketable.getCities("cities/cities_de.txt", 10)
cities = maketable.getCities("cities/cities_us.txt", 20)
distances = maketable.getDistances(cities)
mst = galg.prims(distances)
rst = galg.randSpanningTree(list(distances.keys()))
