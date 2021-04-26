class Graph:
    """
    The purpose of the class is to provide a clean way to define a graph for
    a searching algorithm:
    """

    def __init__(self):
        self.edges = {}  # dictionary of edges NODE: NEIGHBOURS
        self.weights = {}  # dictionary of NODES and their COSTS
        self.herist={}

    def neighbours(self, node):
        """
        The function returns the neighbour of the node passed to it,
        which is essentially the value of the key in the edges dictionary.
        :params node: (string) a node in the graph
        :return: (list) neighbouring nodes
        """

        return self.edges[node]

    def get_cost(self, from_node, to_node):
        """
        Gets the cost of a connection between adjacent nodes.
        :params from_node: (string) starting node
        :params to_node: (string) ending node
        :return: (int)
        """

        return self.weights[(from_node + to_node)]

    def get_h(self, node):
        """
        This function will give our the heuristic from the node to goal.
        :params node: (String) current node / any node
        :return: (int) heuristic to the goal
        """
        return self.herist[node]


if __name__ == "__main__":
    # testing out the graph class
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {
        'A': set(['B','C','D']),
        'B': set(['E','F']),
        'C':set(['G','H']),
        'D':set(['I',"J"]),
        'H':set(['K'])


    }

    # setting up connection costs
    
    graph.herist={'A':3,'B':4,'C':6,'D':5,'E':3,'F':2,'G':7,'H':8,'I':6,'J':7,'K':9}
    print(graph.get_h("A"))


