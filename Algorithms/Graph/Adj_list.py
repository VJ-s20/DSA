"""
Undirected Graph:  
Vertex:["A","B","C","D","E"]
Edges=[("A","B"),("A","C"),("B",'D'),("B","E"),("B","C"),("E","F"),("C","F")]
                  A
                /   \
              /       \
            B -------- C
          /\           |
         /  \          |
        /    \         |
       D       E-------F        
"""


class Graph:
    def __init__(self, nodes, directed=False):
        self.nodes = nodes
        self.directed = directed
        self.adj_list = {}
        for node in self.nodes:
            self.adj_list[node] = []
        

    def add_edges(self, u, v):
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def Node_degree(self, node):
        return f"Degree of {node} is: {len(self.adj_list[node])}"

    def Print_adj_list(self):
        for node in self.adj_list:
            print(node, ":", self.adj_list[node])

#     BFS Traversal
    def bfs_traversal(self,start,path=""):
        visited=[start]
        queue=[start]
        while queue:
            u=queue.pop(0)
            path+=u+" "
            for v in self.adj_list[u]:
                if v not in visited:
                    visited.append(v)
                    queue.append(v)
        return path

    def shortest_path(self,start="A",end="E"):
        parent={}
        visited={}
        for i in self.adj_list:
            parent[i]=None
            visited[i]=False
        queue=[start]
        visited[start]=True
        while queue:
            u=queue.pop(0)
            for v in self.adj_list[u]:
                if not visited[v]:
                    visited[v]=True
                    queue.append(v)
                    parent[v]=u
        path=[]
        while end:
            path.append(end)
            end=parent[end]
        return path[::-1]


    # DFS traversal 
    def __dfs(self,start,color,path):
        color.add(start)
        path.append(start)
        for v in self.adj_list[start]:
            if v not in color:
                self.__dfs(v,color,path)
        return path
    def _dfs(self):
        color=set()
        return self.__dfs("A",color,[])
        
    def dfsUtil(self,visited,v):
        visited[v]=True
        print(v,end=" ")
        for i in self.adj_list[v]:
            if visited[i]==False:
                self.dfsUtil(visited,i)
    def dfs(self):
        visited={}
        for i in self.adj_list:
            visited[i]=False
        return self.dfsUtil(visited,"A")

if __name__ == "__main__":
    all_edges = [("A","B"),("A","C"),("B",'D'),("B","E"),("B","C"),("E","F"),("C","F")]
    graph = Graph(["A", "B", "C", "D", "E","F"])
    for u, v in all_edges:
        graph.add_edges(u, v)
    # graph.Print_adj_list()
    print(graph.shortest_path())
    # print(graph.Node_degree("B"))
    # print(graph.bfs_traversal("A"))
    # print(graph.dfs())

    # graph.dfs()