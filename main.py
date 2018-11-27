import GraphAlgorithms as galg
import maketable
import GA as ga

def write_edgelist(elist):
    with open("edges.csv", "w") as f:
        f.write("start, finish\n")
        for s,t in elist:
            f.write("{},{}\n".format(s,t))

#cities = maketable.getCities("cities/cities_de.txt", 10)
cities = maketable.getCities("cities/cities_us.txt", 20)
distances = maketable.getDistances(cities)
mst = galg.prims(distances)
rst = galg.randSpanningTree(list(distances.keys()))
g = ga.GA(distances)

