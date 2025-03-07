data = open('rosalind_bf.txt', 'r')
rawdata = data.read()
rawdata_1 = rawdata.split('\n')
edge_data = rawdata_1[:-1]
edge_raw = []

for pair in edge_data:
    edge_raw.append(list(map(int, pair.split(' '))))

max_node = edge_raw[0][0]
max_edge = edge_raw[0][1]
edge = edge_raw[1:]

graph = {}
for i in range(max_edge+1):                     #1_based_indexing
    graph[i+1] = {}

for pair in edge:                               #pair[0]: start node, pair[1]: end node, pair[2]: weight
    graph[pair[0]][pair[1]] = pair[2]           #For example. 1 2 4 / 1 3 5 / 1 9 2 /2 3 5-> {1:{2:4, 3:5, 9:2}, 2:{3:5}}


def DIJ(max_node, edge):

    weighted_distance = []
    for i in range(max_node):
        weighted_distance.append([-1, 1000000]) #-1:level, 10^6: max weighted_distance (max_node = 1000, max weight = 1000)
    weighted_distance[0][0] = 0                 #start node level
    weighted_distance[0][1] = 0                 #start node weighted distance

    level = 1
    while True:
        count = 0
        for i in range(max_node):
            if weighted_distance[i][0] == (level - 1):   #BFS
                for arrival_key in graph[i+1]:
                    path = weighted_distance[i][1] + graph[i+1][arrival_key]
                    if path < weighted_distance[arrival_key-1][1]:
                        weighted_distance[arrival_key-1][0] = level
                        weighted_distance[arrival_key-1][1] = path
                        count += 1
        level += 1

        if count == 0:
            break
        
    return weighted_distance

answer = [0]
for pair in DIJ(max_node, edge)[1:]:
    if pair[0] == -1:
        answer.append('x')
    else:
        answer.append(pair[1])

w = open('output_bf.txt', 'w')
w.write(' '.join(map(str, answer)))
w.close()
