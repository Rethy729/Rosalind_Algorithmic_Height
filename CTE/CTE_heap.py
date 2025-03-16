from collections import defaultdict
import heapq

data = open('rosalind_cte.txt', 'r')
rawdata = data.read()
rawdata_split = rawdata.split('\n')
k = int(rawdata_split[0])

def graph(edges):
    graph = defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
    return graph

def CTE(graph, max_node, start_edge):
    distance_lst = [99999999] * (max_node + 1)
    start_node = start_edge[0]
    #distance_lst[start_node] = 99999999
    distance_lst[start_edge[1]] = start_edge[2]
    dij_queue = []
    heapq.heappush(dij_queue, [start_edge[2], start_edge[1]])
    while dij_queue:
        #pick one edge, which has the smallest distance
        dist, node = heapq.heappop(dij_queue)
        if distance_lst[node] < dist:
            continue
        #print (graph[node])
        for arr_node in graph[node]:
            new_dist = distance_lst[node] + graph[node][arr_node]

            if arr_node == start_node:
                if new_dist < distance_lst[start_node]:
                    distance_lst[start_node] = new_dist
            #print (arr_node)
            #print (new_dist)
            elif new_dist < distance_lst[arr_node]:
                distance_lst[arr_node] = new_dist
                heapq.heappush(dij_queue, [distance_lst[arr_node], arr_node])

    if distance_lst[start_node] == 99999999:
        return -1
    else:
        return distance_lst[start_node]

def data_processing(rawdata):
    raw_data = rawdata[1:]
    data_index = 0
    #print (raw_data)
    for i in range(k):
        edges = []
        #print (raw_data[data_index])
        max_node = list(map(int, raw_data[data_index].split(' ')))[0]
        max_edge = list(map(int, raw_data[data_index].split(' ')))[1]

        raw_edge = raw_data[data_index + 1: data_index + 1 + max_edge]
        data_index += max_edge + 1
        for pair in raw_edge:
            edges.append(list(map(int, pair.split(' '))))

        start_edge = edges[0]
        graph_data = graph(edges)
       # print (graph_data)
        print (CTE(graph_data, max_node, start_edge), end = ' ')

data_processing(rawdata_split)