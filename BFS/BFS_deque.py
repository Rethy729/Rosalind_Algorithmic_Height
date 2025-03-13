from collections import deque

f = open('rosalind_bfs.txt', 'r')
data = f.readlines()

def graph(data):
    max_node = list(map(int, data[0].strip().split(' ')))[0]
    #max_edge = list(map(int, data[0].strip().split(' ')))[1]
    edges = []
    for line in data[1:]:
        edges.append(list(map(int, line.strip().split(' '))))

    graph = {}
    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
    return max_node, graph

max_node, graph = (graph(data))
print (graph)

def BFS(max_node, graph):
    distance_lst = [-1] * (max_node + 1)
    bfs_queue = deque()
    distance_lst[1] = 0
    bfs_queue.append(1)
    while bfs_queue:
        v = bfs_queue.popleft()
        if v in graph:
            for arr_node in graph[v]:
                if distance_lst[arr_node] == -1:
                    bfs_queue.append(arr_node)
                    distance_lst[arr_node] = distance_lst[v] + 1

    return distance_lst[1:]

print (' '.join(map(str, BFS(max_node, graph))))





