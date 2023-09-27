import copy

# Read the entries for the graph in graph.txt archive
# Using a adjacence list for representation
def readGraph():
    graph = []
    k = 0
    target = True

    with open('graph.txt') as graphText:
        for index, line in enumerate(graphText):
            if index == 0:
                k = int(line)
                continue
            if target == True:
                adjac = []
                for vertex in line.split():
                    adjac.append(int(vertex))
                graph.append(adjac)
        print(graph)

    return graph, k

# Begin of the algorithm
# Pick a random vertex of graph and put your
# adjacences in a list for the next step of the 
# algorithm
def enumerateSubgraph():
    used = []
    for i in graph:
        used.append(0)
    for v in range(len(graph)):
        vExtension = set()
        for v_adj in graph[v]:
            if v_adj > v:
                vExtension.add(v_adj)
        extendSubgraph([v], vExtension, v, used[:])


def extendSubgraph(subGraph, vExtension, v, used):
    # Check if subGraph has size equals to k
    # Sum 1 to the number of subGraphs founded
    if len(subGraph) == k:
        print("SubGraph: ",sorted(subGraph), "\n")
        global subTotal
        subTotal += 1
        return

    # Take a vertex of vExtension and copy all of your
    # adjacences to a new vExtension
    # Try to expand the subGraph with the possibilities
    # founded in vExtension
    while len(vExtension) != 0:
        w = vExtension.pop()
        vExtension2 =copy.deepcopy(vExtension)
        used[w] = -1
        used2 = used[:]

        for u in graph[w]:
            if u not in subGraph and u > v and used[u] == 0:
                vExtension2.add(u)

        subGraph.append(w)
        extendSubgraph(subGraph, vExtension2, v, used2)
        subGraph.pop(-1)

graph, k = readGraph()
subTotal = int(0)
enumerateSubgraph()

print(f"Total number of subGraphs: {subTotal}")
