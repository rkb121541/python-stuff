from adj_list import adjacency_list_dict
from collections import deque

def DFS(V, edges):
    vertices = {}
    for vertex in V:
        vertices[vertex] = 0
    count = 0
    for vertex in V:
        if vertices[vertex] == 0:
            stack = [vertex]
            while stack:
                u = stack.pop()
                if vertices[u] == 0: 
                    count += 1
                    vertices[u] = count
                    for edge in edges:
                        if edge[0] == u and vertices[edge[1]] == 0:
                            stack.append(edge[1])

    return vertices
            



if __name__ == "__main__":
    V = [1,2,3,4,5,6,7,8,9,10]
    edges = [[1,2],[1,4],[2,5],[4,2],[4,5],[5,3],[5,9],[6,8],[7,10],[9,7],[9,10],[10,3]]
    print(DFS(V, edges)) 
