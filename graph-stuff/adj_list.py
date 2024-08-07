# 1: 2, 4
# 2: 5
# 3:
# 4: 2, 5
# 5: 3, 9
# 6: 8
# 7: 10
# 8:
# 9: 7, 10
# 10: 3

def adjacency_list_dict(V, edges):
    adjacency_list = {}

    for vertex in V:
        adjacency_list[vertex] = []

    for edge in edges:
        vertex1, vertex2 = edge
        adjacency_list[vertex1].append(vertex2)

    for vertex, neighbors in adjacency_list.items():
        print(f"{vertex} -> {', '.join(map(str, neighbors))}")
    
if __name__ == "__main__":
    V = [1,2,3,4,5,6,7,8,9,10]
    edges = [[1,2],[1,4],[2,5],[4,2],[4,5],[5,3],[5,9],[6,8],[7,10],[9,7],[9,10],[10,3]]
    adjacency_list_dict(V, edges) 
