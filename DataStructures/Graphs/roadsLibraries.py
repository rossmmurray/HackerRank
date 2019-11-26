#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# problem earlier today
# given a list of routes a->b, b->c etc. find all paths from c->d
# unweighted
# he suggested to do an adjacency list {a: [b, d f], b: [a, c], ...}
# you could have done a adjacency matrix [[true, false, ...], ...] etc.

# notes
# put a library somewhere, 
# go to next node
# if c_road * steps < c_lib
# if c_road is smaller than clib you should always build one library and all the roads
# check how many connected subgraphs
# treat as unweighted graph
# fin spanning trees unweighted
# n_subgraphs * clib + n_subgraphs * (n_edges1 - 1 + n_edges2 - 1)
# if croad > clib, build a lib at every node so n * clib


# do an adjacency list or adjacency component

# create adjacency list
# pick some node to begin
# do depth first search, visiting only unvisited nodes
# visited[] array with boolean values to track visited nodes
# go to next unvisited node and do the same

def createAdjacencyList(cities):
    adjList = defaultdict(list)
    for route in cities:
        adjList[route[0]].append(route[1])
        adjList[route[1]].append(route[0])
    return adjList

def depthFirstSearch(city, adjCities, visited):
    visited[city] = True
    edges = 0
    for city in adjCities[city]:
        if not visited[city]:
            edges += 1 + depthFirstSearch(city, adjCities, visited)
    return edges


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    # if the cost of building a library is cheaper than a road, it's cheapest to build a library at each city
    # if c_lib < c_road:
    #     return n * c_lib

    # create adjacency and visited lists
    adjList = createAdjacencyList(cities)
    visited = {i: False for i in adjList}

    # do depth first search from each node, setting visited bools and counting edges
    newEdges = 0
    for city in adjList:
        # i think visited will just update so just return number of new edjest
        newEdges += depthFirstSearch(city, adjList, visited)
    print(newEdges)


    
    # find spanning trees for the graph(s)
    # connected_components = []
    # for route in cities:
    #     if len(connected_components) == 0:
    #         connected_components.append([route])
    #     else:
    #         for connected_component in connected_components:
    #             # check if both nodes are in a component

    #             # check if either node is in connected components
    #             if route[0] in connected_component or route[1] in connected_component:
    #                 connected_component.append(route)






    print("number of cities, n: " + str(n)) 
    print("cost of library, c_lib: " + str(c_lib))
    print("cost of road repair, c_road: " + str(c_road)) 
    print("edges aka cities: " + str(cities))
    return 50000

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)

        fptr.write(str(result) + '\n')

    fptr.close()
