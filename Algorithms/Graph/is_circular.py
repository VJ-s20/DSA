"""
Undirected Graph
vertex=['A','B','C','D','F']
Edges: {'A': ['B', 'D'], 'B': ['C'], 'C': ['A', 'F']}
 A --------->D
 | /\
 |    \
\|/     \
 B-------->C------>F
"""

edge = {'A': ['B', 'D'], 'B': ['C'], 'C': ['A', 'F'], 'F': [], 'D': []}  # Directed Graph
edge={'A': ['B', 'D'], 'B': ['A','C'], 'C': ['A','B', 'F'], 'F': ['C'], 'D': ['A']} # Undirected graph


def _isCirular(visited,parent,u):
    visited[u]=True
    for v in edge[u]:
        if not visited[v]:
            parent[v]=u
            _isCirular(visited,parent,v)
        elif visited[v] and parent[u]!=v:  #! If the parent of the vertex u and current vertex v is not the same it's means there is cycle present
            print(u,v)
            return True

def is_circular():
    visited={}
    parent={}
    for node in edge:
        parent[node]=None
        visited[node]=False
    return _isCirular(visited,parent,'A')

if __name__=="__main__":
    is_circular()