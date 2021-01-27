

class Graph:
    def __init__(self,nodes) -> None:
        self.nodes=nodes
        self.adj_list={}
        for start,end in self.nodes:
            if start in self.adj_list:
                self.adj_list[start].append(end)
            else:
                self.adj_list[start]=[end]


    def get_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path

        elif start not in self.adj_list:
            return None

        paths = ""
        for node in self.adj_list[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                paths+=str(new_paths)+"\n"
        return paths

    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]
        if start==end:
            return path
        if start not in self.adj_list:
            return None
        shortest_path=None
        for node in self.adj_list[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if not shortest_path or len(sp) < len(shortest_path):
                    shortest_path = sp
        return shortest_path




if __name__ == '__main__':

    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    graph=Graph(routes)
    # print(graph.adj_list)
    start="Mumbai"
    end="New York"
    # print(graph.get_path(start,end))
    print(graph.get_shortest_path(start,end))