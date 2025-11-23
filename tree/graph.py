import random


class Graph:
    """
    Adjacency List
    """

    def __init__(self, nodes=[]):
        self.nodes = nodes

    def add_nodes(self, nodes):
        self.nodes.extend(nodes)

    def print_nodes(self):
        for node in self.nodes:
            node.print_node()
        return

    def dfs(self, visit):
        def search(node):
            if node and not node.visited:
                visit(node)
                node.visited = True
                for neighbor in node.neighbors:
                    search(neighbor)
            return

        print("--Start DFS--")
        for node in self.nodes:
            search(node)
        print("--End DFS--")
        return

    def bfs(self, visit):
        """Perform breadth first search on the graph. If a node is visited, it is assumed that all children are visited because a parent is always visited before adding the child. The only way that this is not the case is multiple parents having the same child, which is not possible.

        Args:
            visit (callable): visiting function
        Return:
            None
        """

        def search(root):
            q = []
            root.visited = True
            visit(root)
            q.append(root)
            while q:
                curr_node = q.pop(0)
                for neighbor in curr_node.neighbors:
                    if not neighbor.visited:
                        neighbor.visited = True
                        visit(neighbor)
                        q.append(neighbor)

        print("--Start BFS--")
        for root in self.nodes:
            search(root)
        print("--End BFS--")
        return


class GraphNode:
    """
    Graph Node for Adjacency List
    """

    def __init__(self, value=-1, neighbors=[]):
        self.value = value
        self.visited = False
        self.neighbors = neighbors

    def add_neighbor(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)

    def print_node(self):
        print(
            f"node: {self.value}, visited: {self.visited}, neighbors: {[neighbor.value for neighbor in self.neighbors]}"
        )


class GraphMatrix:
    def __init__(self, matrix):
        if not matrix:
            raise Exception("Matrix needs to be predefined")
        self.matrix = matrix


def gen_random_nums_with_replacement(num, start, end):
    res = []
    for i in range(num):
        new_random = random.randint(start, end)
        while new_random in res:
            new_random = random.randint(start, end)
        res.append(random.randint(start, end))
    return res


def gen_random_graph(directed=False, num_nodes=-1, num_vertex=-1):
    v = num_nodes if num_nodes != -1 else random.randint(1, 10)
    e = (
        num_vertex
        if num_vertex != -1
        else random.randint(0, (v * (v - 1)) / 2)
    )
    all_nodes = [GraphNode(i) for i in range(1, v + 1)]
    new_graph = Graph(all_nodes)
    new_graph.print_nodes()
    for _ in range(e):
        i1 = random.randint(1, v) - 1
        i2 = random.randint(1, v) - 1
        while i1 == i2:
            i2 = random.randint(0, v - 1)
        print(f"i1 {i1}, i2 {i2}")
        all_nodes[i1 - 1].add_neighbor(all_nodes[i2])
        if not directed:
            all_nodes[i2 - 1].add_neighbor(all_nodes[i1])
        new_graph.print_nodes()
    return new_graph


if __name__ == "__main__":
    new_graph = gen_random_graph(directed=False, num_nodes=8)
