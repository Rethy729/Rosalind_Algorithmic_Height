import heapq

#the dataset in Rosalind includes some awful nodes like : 234 546 133 /  234 546 664 -> in this case, we have to leave the minimum weight among the repeated appearance of edge

f = open('rosalind_bf.txt', 'r')
data = f.readlines()

def graph(data):
    max_node = list(map(int, data[0].strip().split(' ')))[0]
    #max_edge = list(map(int, data[0].strip().split(' ')))[1]
    edges = []
    for line in data[1:]:
        edges.append(list(map(int, line.strip().split(' '))))

    graph = {}
    for i in range(max_node + 1):  # 1_based_indexing
        graph[i + 1] = {}

    for edge in edges: # pair[0]: start node, pair[1]: end node, pair[2]: weight
        if edge[1] in graph[edge[0]]:
            if edge[2] < graph[edge[0]][edge[1]]:
                graph[edge[0]][edge[1]] = edge[2]
        else:
            graph[edge[0]][edge[1]] = edge[2] #For example. 1 2 4 / 1 3 5 / 1 9 2 /2 3 5-> {1:{2:4, 3:5, 9:2}, 2:{3:5}}

    return max_node, graph

max_node, graph = (graph(data))
print (graph)

def DIJ(graph, max_node):

    distance_lst = [99999999] * (max_node + 1)
    distance_lst[1] = 0
    dij_queue = []
    heapq.heappush(dij_queue, [distance_lst[1], 1])
    #initializing, insert [0, 1] in dij_queue

    while dij_queue:
        #pick one edge, which has the smallest distance
        dist, node = heapq.heappop(dij_queue)
        #print (dist, node)

        if distance_lst[node] < dist:
            continue

        #print (graph[node])
        for arr_node in graph[node]:
            #print (arr_node)
            new_dist = distance_lst[node] + graph[node][arr_node]
            #print (new_dist)
            if new_dist < distance_lst[arr_node]:
                distance_lst[arr_node] = new_dist
                heapq.heappush(dij_queue, [distance_lst[arr_node], arr_node])

    for i in range(max_node+1):
        if distance_lst[i] == 99999999:
            distance_lst[i] = 'x'
    return distance_lst[1:]

print (len(DIJ(graph, max_node)))
print (' '.join(map(str, DIJ(graph, max_node))))