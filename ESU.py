#Read the entries for a graph
#Using adjacence list
def readGraph():
    graph = []
    for i in range(5):
        x = input()
        vertex = []
        for i in x.split():
            vertex.append(int(i))
        graph.append(vertex)
    return graph


#Initial function of ESU algorithm
#Select the initial vertex of the list
def enumerateSubgraph( graph, k ):
    for indice, v in enumerate(graph):
        vExtension = []
        father = [-1]
        subGraph = [indice]
        vertexIn = [indice]
        for u in v:
            if u > indice:
                twin = [u,indice]
                vExtension.append(twin)    
        #print(vExtension)
        extendSubgraph(graph, subGraph, vExtension, vertexIn, father, indice, k)


# Recursive function to find all of the subGraphs that contains
# the vertex k, and doesn't contain vertex < k
def extendSubgraph(graph, subGraph, vExtension, vertexIn, father, indice, k):
    if len(vertexIn) == k:
        print("Encontrado: \n\t", subGraph, "\n\t", father, "\n")
        return 

    while len(vExtension) != 0:
        #print("Etapa: \n\tSubGraph: ", subGraph)
        #print("\tvExtension: ", vExtension, "\n")

        w = vExtension.pop(0)
        w0 = w[0]
        w1 = w[1]

        subGraph2 = subGraph[:]
        vExtension2 = vExtension[:]
        father2 = father[:]
        vertexIn2 = vertexIn[:]

        for u in graph[w0]:
            if u not in subGraph and u > indice:
                twin = [u, w0]
                vExtension2.append(twin)
        if w0 not in subGraph:
            vertexIn2.append(w0)

        subGraph2.append(w0)
        father2.append(w1)

        extendSubgraph(graph, subGraph2, vExtension2, vertexIn2, father2, indice, k)

# Initial call to the algorithm
# The example is made by a graph of size 5, five vertex
enumerateSubgraph(readGraph(), int(input()))
