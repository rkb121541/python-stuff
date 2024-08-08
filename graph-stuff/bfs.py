from adj_list import adjacency_list_dict
from collections import deque

def BFS(V, edges):
    vertices = {}
    for vertex in V:
        vertices[vertex] = 0
    count = 0
    for vertex in V:
        if vertices[vertex] == 0:
            count += 1
            q = deque()
            q.append(vertex)
            vertices[vertex] = count
            while q:
                u = q.popleft()
                for src, dst in edges:
                    if src == u and vertices[dst] == 0:
                        count += 1
                        vertices[dst] = count
                        q.append(dst)

    return vertices
            



if __name__ == "__main__":
    V = [1,2,3,4,5,6,7,8,9,10]
    edges = [[1,2],[1,4],[2,5],[4,2],[4,5],[5,3],[5,9],[6,8],[7,10],[9,7],[9,10],[10,3]]
    print(BFS(V, edges)) 
