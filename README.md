# GraphGA: An Evolutionary Algorithm to Develop Transportation Networks

Graph algorithms evoke memories of my time as a truck driver and dispatcher and of childhood family vacations.
Many graph algorithms result in minimum weight trees, which are good for designing a shortest single path. However, I wanted
to find an algorithm to devise a whole transportation network that would minimize routing cost for all users. Minimum Spanning
Trees find routes that are lowest cost to build but likely have prohibitive use costs for some users.

As an alternative, I propose All-Pairs-Shortest-Paths-Cost as a metric. The metric is calculated simply by summing all entries in the cost matrix resulting from the all-pairs-shortest-paths algorithm.  There are two APSP-Costs, one to the network builders, 
the other to the users. My final multiobjective function is the user cost of the proposed network times the ratio between the build cost of the propsed network and build cost of a baseline network devised by applying Prim's algorithm.

I implemented in Python a genetic algorithm to evolve optimal networks. The graphs were represented as edge-lists, 
which required devising original mutation and recombination algorithms. I wrote my own implementations of Prim's and
All-Pairs-Shortest-Paths, using the explanations in CLRF as a reference.

The maps in the pdf write-up of the project are the output of some scripting I did in R-Studio. I was taking a statistics
class at the time of this project which utilitzed R. I had some help from my instructor in writing effecient R loops.

The algorithm and the objective function succeded in finding viable transport solutions.

This was submitted as the final project of a class in Genetic Algorithms. The idea for the project was my own.
