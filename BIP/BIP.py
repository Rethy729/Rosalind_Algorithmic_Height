from collections import deque

f = open('rosalind_bip.txt', 'r')
data = f.read()
data_split = data[:-1].split('\n\n')

def graph(max_node, edges):
    graph = {}
    for i in range(max_node):
        graph[i + 1] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

def BFS(graph, start_node, distance_lst):
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
                elif (distance_lst[arr_node] - distance_lst[v]) % 2 == 0:
                    return -1, distance_lst
    return 1, distance_lst

def data_processing(data):
    n = int(data[0])
    answer = []
    for chunk in data[1:]:
        edges = list(map(str, chunk.split('\n')))
        max_node = list(map(int, edges[0].split()))[0]
        edges_data = []
        for edge in edges[1:]:
            edges_data.append(list(map(int, edge.split())))

        graph_data = graph(max_node, edges_data)
        #print (graph_data)
        distance_lst = [-1] * (max_node + 1)
        distance_lst[0] = -2
        start_node = 1
        bip = 0

        while -1 in distance_lst:
            bip, distance_lst = BFS(graph_data, start_node, distance_lst)
            if bip == -1:
                break
            for i, dist in enumerate(distance_lst):
                if dist == -1:
                    start_node = i
        answer.append(bip)
    return answer

print (' '.join(map(str, data_processing(data_split))))