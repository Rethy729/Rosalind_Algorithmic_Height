from collections import deque

f = open('rosalind_cc.txt', 'r')
data = f.readlines()

def graph(data):
    edges = []
    max_node = list(map(int, data[0].strip().split(' ')))[0]
    edge_num = list(map(int, data[0].strip().split(' ')))[1]
    for line in data[1:]:
        edges.append(list(map(int, line.strip().split(' '))))

    graph = {}
    for i in range(max_node):
        graph[i + 1] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return max_node, graph

max_node, graph = graph(data)

def DFS(start_node, visited_bool, cc):
    dfs_stack = deque()
    dfs_stack.append(start_node)
    while dfs_stack:
        v = dfs_stack.pop()
        if visited_bool[v] == False:
            visited_bool[v] = True
            cc.append(v)
            for arr_node in graph[v]:
                dfs_stack.append(arr_node)


visited_bool = [False] * ((max_node)+1)
total_components = []
for i in range(1, max_node+1):
    cc = []
    if visited_bool[i] == False:
        DFS(i, visited_bool, cc)
        total_components.append(cc)

print (len(total_components))