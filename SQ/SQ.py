from itertools import combinations

f = open('rosalind_sq.txt', 'r')
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

def find_square(graph):
    neighbor_set = set()
    for node in graph:
        for i, j in combinations(graph[node], 2):
            neighbor_pair = (i, j)
            if neighbor_pair in neighbor_set:
                return 1
            else:
                neighbor_set.add(neighbor_pair)
    return -1

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
        answer.append(find_square(graph_data))
    return answer

print(' '.join(map(str, data_processing(data_split))))