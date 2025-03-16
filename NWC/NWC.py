import heapq

data = open('rosalind_nwc.txt', 'r')
rawdata = data.read()
rawdata_split = rawdata.split('\n')
k = int(rawdata_split[0])

def graph(edges, max_node):
    graph = []
    for edge in edges:
        graph.append(edge)
    for i in range(1, max_node+1):
        graph.append([max_node+1, i, 0])
    return graph, len(graph)

def NWC(graph, max_node, max_edge, start_node):
    distance_lst = [99999999] * (max_node+1)
    distance_lst[start_node] = 0
    for i in range(max_node):
        for j in range(max_edge):
            current_node = graph[j][0]
            arr_node = graph[j][1]
            weight = graph[j][2]

            if distance_lst[current_node] != 99999999 and distance_lst[arr_node] > distance_lst[current_node] + weight:
                distance_lst[arr_node] = distance_lst[current_node] + weight
                if i == max_node-1:
                    return 1
    return -1

def data_processing(rawdata):
    raw_data = rawdata[1:]
    data_index = 0
    for i in range(k):
        edges = []
        max_node = list(map(int, raw_data[data_index].split(' ')))[0]
        max_edge = list(map(int, raw_data[data_index].split(' ')))[1]

        raw_edge = raw_data[data_index + 1: data_index + 1 + max_edge]
        data_index += max_edge + 1
        for pair in raw_edge:
            edges.append(list(map(int, pair.split(' '))))

        graph_data, max_edge_new = graph(edges, max_node)

        #print (graph_data)
        print (NWC(graph_data, max_node+1, max_edge_new, max_node+1), end= ' ')

data_processing(rawdata_split)