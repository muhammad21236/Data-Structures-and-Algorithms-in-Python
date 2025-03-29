class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} : {self.adj_list[vertex]}")

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def bfs(self, start):
        """
        Breadth-First Search (BFS) traverses the graph level by level.
        It uses a queue to visit all neighbors of a node before moving to the next level.
        """
        if start not in self.adj_list:
            return []
        visited = set()
        queue = [start]
        result = []
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([neighbor for neighbor in self.adj_list[vertex] if neighbor not in visited])
        return result

    def dfs(self, start):
        """
        Depth-First Search (DFS) traverses the graph by exploring as far as possible
        along each branch before backtracking. It uses recursion.
        """
        def dfs_recursive(vertex, visited, result):
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.adj_list[vertex]:
                    dfs_recursive(neighbor, visited, result)
        
        if start not in self.adj_list:
            return []
        visited = set()
        result = []
        dfs_recursive(start, visited, result)
        return result

# Example usage
my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("C", "D")
my_graph.add_edge("B", "D")

my_graph.print_graph()

print("BFS Traversal:", my_graph.bfs("A"))
print("DFS Traversal:", my_graph.dfs("A"))
