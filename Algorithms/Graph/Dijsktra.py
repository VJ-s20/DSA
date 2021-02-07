'''
Dijkstra’s algorithm is very similar to Prim’s algorithm for minimum spanning tree. Like Prim’s MST, we generate a SPT (shortest path tree) with given source as root. We maintain two sets, one set contains vertices included in shortest path tree, other set includes vertices not yet included in shortest path tree. At every step of the algorithm, we find a vertex which is in the other set (set of not yet included) and has a minimum distance from the source.

Below are the detailed steps used in Dijkstra’s algorithm to find the shortest path from a single source vertex to all other vertices in the given graph.
Algorithm
1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty.
2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first.
3) While sptSet doesn’t include all vertices
….a) Pick a vertex u which is not there in sptSet and has minimum distance value.
….b) Include u to sptSet.
….c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex v, if sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.

                3
             a<-----f
      10 ./     \.3
         b<----->c
         |    /  | 
        .|. /.   |.
         d<----->e 
'''
def shortest_path(distance,parent,start,goal):
    currentNode=goal
    path=[]
    while currentNode:
        path.append(currentNode)
        currentNode=parent[currentNode]
    if distance[goal]!=float('inf'):
        print(f'Shortest Distance from {start} to {goal}: {distance[goal]}')
        print('Path is:', path[::-1])
    else:
        print("Goal Not Reacheable")

def dijsktra_path(graph,start,end):
    parent={}
    shortest_distance={}
    for node in graph:
        parent[node]=None
        shortest_distance[node]=float('inf')
    shortest_distance[start]=0
    while graph:
        minNode=None
        for node in graph:
            if not minNode:
                minNode=node
            elif shortest_distance[node]<shortest_distance[minNode]:
                minNode=node
        for chlidNode,weight in graph[minNode].items():
            if weight+shortest_distance[minNode]<shortest_distance[chlidNode]:
                shortest_distance[chlidNode]=weight+shortest_distance[minNode]
                parent[chlidNode]=minNode
        graph.pop(minNode)
    return shortest_path(shortest_distance,parent,start,end)

if __name__=="__main__":
    graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {
        'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9},'f':{'a':3}}
    dj=dijsktra_path(graph,'a','e')

