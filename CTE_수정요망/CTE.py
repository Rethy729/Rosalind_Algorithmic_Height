data = open('rosalind_cte.txt', 'r')
rawdata = data.read()
rawdata_split = rawdata.split('\n')
k = int(rawdata_split[0])

def Short_Cycle(max_node, graph, edge):
    
    search_end_node = edge[0][0]    #first specified edge initialization
    search_start_node = edge[0][1]
    start_weight = edge[0][2]
    
    weighted_distance = []
    for i in range(max_node+1):
        weighted_distance.append([-1, 1000000]) #-1:level, 10^6: max weighted_distance (max_node = 1000, max weight = 1000)
    weighted_distance[search_start_node][0] = 0                 #start node level initialization
    weighted_distance[search_start_node][1] = start_weight      #start node weighted distance initialization
    
    level = 1
    while True:
        count = 0
        for i in range(1, max_node+1):
            if weighted_distance[i][0] == (level - 1):     #BFS
                for arrival_key in graph[i]:
                    path = weighted_distance[i][1] + graph[i][arrival_key]
                    if path < weighted_distance[arrival_key][1]:
                        weighted_distance[arrival_key][0] = level
                        weighted_distance[arrival_key][1] = path
                        count += 1
        level += 1

        if count == 0: #if BFS ends, break the while loop
            break

    if weighted_distance[search_end_node][0] == -1:
        return -1
    else:
        return weighted_distance[search_end_node][1]

answer = []

raw_data = rawdata_split[1:]
data_index = 0 
for i in range(k):
    edge = []
    max_node = list(map(int, raw_data[data_index].split(' ')))[0]
    max_edge = list(map(int, raw_data[data_index].split(' ')))[1]

    raw_edge = raw_data[data_index+1 : data_index+1+max_edge]
    data_index += max_edge+1
    for pair in raw_edge:
        edge.append(list(map(int, pair.split(' '))))

    graph = {}
    for i in range(max_node+1):
        graph[i+1] = {}                              #1_based_indexing

    for pair in edge:                                #pair[0]: start node, pair[1]: end node, pair[2]: weight
        graph[pair[0]][pair[1]] = pair[2]            #For example. 1 2 4 / 1 3 5 / 1 9 2 /2 3 5-> {1:{2:4, 3:5, 9:2}, 2:{3:5}}
    
    answer.append(Short_Cycle(max_node, graph, edge))

print (' '.join(map(str, answer)))
