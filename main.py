import GraphAlgorithms as galg
from statistics import mean, stdev
import maketable
import random
#import GA as ga
from EdgeGA import EdgeGA as ga

run = 0
map_s = "au50"

def write_edgelist(elist):
    with open("edges.csv", "w") as f:
        f.write("start, finish\n")
        for s,t in elist:
            f.write("{},{}\n".format(s,t))

def report_s(f, g):
    s = "{}, {}, {}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(map_s, g.generation, run, min(f), mean(f), stdev(f), max(f))
    return s

#cities = maketable.getCities("cities/cities_de.txt", 10)
cities = maketable.getCities("cities/cities_au.txt", 50)
distances = maketable.getDistances(cities)
#mst = galg.prims(distances)
#rst = galg.randSpanningTree(list(distances.keys()))

best = None
best_fit = 0

for run in range(1,26):
    g = ga(distances)
    fits = [x['fitness'] for x in g.heap.heap[1:]]
    s = report_s(fits,g)
    print(s)
    with open("output/au50_output.csv", "a") as f:
       f.write(s)
    for _ in range(100):
        g.evolve()
        fits = [x['fitness'] for x in g.heap.heap[1:]]
        s = report_s(fits,g)
        print(s)
        with open("output/au50_output.csv", "a") as f:
           f.write(s)
        if stdev(fits) < 400:
            break
    fits = [x['fitness'] for x in g.heap.heap[1:]]
    if max(fits) > best_fit:
        best_fit = max(fits)
        for x in g.heap.heap[1:]:
            if x['fitness'] == max(fits):
                best = x['chr']

with open("output/best.csv", "a") as f:
    for s,t in best:
        f.write("{},{},{}\n".format(map_s, s, t))


