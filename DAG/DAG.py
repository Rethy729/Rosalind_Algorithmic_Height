from collections import deque

f = open('rosalind_dag.txt', 'r')
data = f.read()
data_split = data[:-1].split('\n\n')
def graph(max_node, edges):
    graph = {}
    for i in range(max_node):
        graph[i + 1] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])

    return graph

def DFS(graph, start_node, visited_bool):

    dfs_stack = deque()
    dfs_stack.append(start_node)
    cc = []
    while dfs_stack:
        v = dfs_stack.pop()
        cc.append(v)
        if visited_bool[v] == False:
            visited_bool[v] = True
            for arr_node in graph[v]:
                if arr_node == start_node:
                    return cc, True
                else:
                    dfs_stack.append(arr_node)
                    cc.append(arr_node)
    return cc, False

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
        visited_bool = [False] * (max_node + 1)
        cycle_bool = False
        for i in range(1, max_node + 1):
            if visited_bool[i] == False:
                cc, cycle_bool = DFS(graph_data, i, visited_bool)
                if cycle_bool:
                    answer.append(-1)
                    break
                elif not cycle_bool:
                    for node in cc:
                        visited_bool[node] = True
        if not cycle_bool:
            answer.append(1)

    return answer

w = open('output_dag.txt', 'w')
w.write((' '.join(map(str, data_processing(data_split)))))
w.close()