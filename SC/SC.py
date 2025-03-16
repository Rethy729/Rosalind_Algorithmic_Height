from collections import defaultdict
from collections import deque

f = open('rosalind_sc.txt', 'r')
data = f.read()
data_split = data[:-1].split('\n\n')

def graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
    return graph

def BFS(max_node, graph, start_node):
    distance_lst = [-1] * (max_node + 1)
    bfs_queue = deque()
    distance_lst[start_node] = 0
    bfs_queue.append(start_node)
    while bfs_queue:
        v = bfs_queue.popleft()
        if v in graph:
            for arr_node in graph[v]:
                if distance_lst[arr_node] == -1:
                    bfs_queue.append(arr_node)
                    distance_lst[arr_node] = distance_lst[v] + 1

    return distance_lst[1:]

def semi_connected(max_node, graph):

    matrix = []
    for i in range(1, max_node + 1):
        matrix.append(BFS(max_node, graph, i))

    for i in range(max_node):
        for j in range(i, max_node):
            if matrix[i][j] == -1 and matrix[j][i] == -1:
                return -1

    return 1

def data_processing(data):
    for chunk in data[1:]:
        edges = list(map(str, chunk.split('\n')))
        max_node = list(map(int, edges[0].split(' ')))[0]
        edges_data = []
        for edge in edges[1:]:
            edges_data.append(list(map(int, edge.split())))

        graph_data = graph(edges_data)
        print (semi_connected(max_node, graph_data), end = ' ')

data_processing(data_split)
