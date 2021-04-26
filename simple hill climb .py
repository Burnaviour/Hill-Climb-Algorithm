from graph import Graph
import operator
"""
# A is the root node with B, C, D as successors
(A,3) -> (B, 4), (C, 6), (D, 5)
(B,4) -> (E, 3), (F, 2)
(C,6) -> (G, 7), (H, 8)
(D,5) -> (I, 6), (J, 7)
(H,8) -> (K, 9)
Initial node to start is "A" and the goal node is "K"
"""
def hill_climb_search(start,graph,goal):
    current=start
    frontier=[]
    if start==goal:
        return start

    else:
        frontier.append(start)
        while current!=goal:


            neighobours=graph.neighbours(current)

            pl = dict()
            for j in neighobours:
                pl[j]=int(graph.get_h(j))


            max_key = max(pl, key=pl.get)
            if max_key>current:
                current=max_key
                frontier.append(current)
        return frontier

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

    print("path found",hill_climb_search("A",graph,"K"))


