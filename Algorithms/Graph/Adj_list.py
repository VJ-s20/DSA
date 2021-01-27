"""
Undirected Graph:  
Vertex:["A","B","C","D","E"]
Edges=[("A","B"),("A","C"),("C","D"),("D",'B'),("B","E"),("D","E")]
A-------------B__
|             |  ___
|             |      E
|             |  ___
C-------------D__
"""
class Graph:
    def __init__(self,nodes,directed=False) -> None:
        self.nodes=nodes
        self.directed=directed
        self.adj_list={}
        for node in self.nodes:
            self.adj_list[node]=[]

    def add_edges(self,u,v):
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)
    

    def Node_degree(self,node):
        return f"Degree of {node} is: {len(self.adj_list[node])}"


    def Print_adj_list(self):
        for node in self.adj_list:
            print(node,":",self.adj_list[node])

    

if __name__ =="__main__":
    all_edges=[("A","B"),("A","C"),("C","D"),("D",'B'),("B","E"),("D","E"),("A","B")]
    graph=Graph(["A","B","C","D","E"])
    for u,v in all_edges:
        graph.add_edges(u,v)
    graph.Print_adj_list()
    print(graph.Node_degree("B"))

