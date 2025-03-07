data = open('rosalind_bfs.txt', 'r')
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
for i in range(max_edge+1):
    graph[i+1] = [] #1_based indexing

for pair in edge:
    graph[pair[0]].append(pair[1])

def BFS(max_node):
    
    distance = [-1] * max_node
    distance[0] = 0 #start node
    
    distance_temp = 1
    while True:
        count = 0
        for i in range(max_node):                            
            if distance[i] == (distance_temp-1):
                for arrival in graph[i+1]:
                    if distance[arrival-1] == -1:
                        distance[arrival-1] = distance_temp    
                        count += 1
        distance_temp += 1
        if count == 0:
            break
        
    return distance

w = open('output_bfs.txt', 'w')
w.write(' '.join(map(str, BFS(max_node))))
w.close()

