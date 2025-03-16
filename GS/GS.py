from collections import defaultdict
from collections import deque

f = open('rosalind_gs.txt', 'r')
data = f.read()
data_split = data[:-1].split('\n\n')

def graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
    return graph

def DFS(start_node, graph, visited_bool):
    dfs_stack = deque()
    dfs_stack.append(start_node)
    while dfs_stack:
        v = dfs_stack.pop()
        if visited_bool[v] == False:
            visited_bool[v] = True
            for arr_node in graph[v]:
                dfs_stack.append(arr_node)

def data_processing(data):
    for chunk in data[1:]:
        edges = list(map(str, chunk.split('\n')))
        max_node = list(map(int, edges[0].split(' ')))[0]
        edges_data = []
        for edge in edges[1:]:
            edges_data.append(list(map(int, edge.split())))

        graph_data = graph(edges_data)
        sink = [0]*(max_node+1)
        for i in range(1, max_node + 1):
            visited_bool = [False] * (max_node + 1)
            DFS(i, graph_data, visited_bool)
            if False in visited_bool[1:]:
                sink[i] = -1
            else:
                sink[i] = 1
        if 1 in sink:
            print (sink.index(1), end = ' ')
        else:
            print (-1, end = ' ')
data_processing(data_split)

