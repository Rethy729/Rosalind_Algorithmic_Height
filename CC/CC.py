data = open('rosalind_cc.txt', 'r')
rawdata = data.read()
rawdata_split = rawdata.split('\n')
edge = []

for pair in rawdata_split[:-1]:
    edge.append(list(map(int, pair.split(' '))))

node_max = edge[0][0]
edges = edge[1:]

graph = {}
for i in range(node_max):
    graph[i+1] = []

for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

#print (graph)

visited_bool = [False] * (node_max+1)

def DFS(node, visited_bool, connected):
    
    visited_bool[node] = True
    connected.append(node)
    
    for nodes in graph[node]:
        if visited_bool[nodes] == False:
            DFS(nodes, visited_bool, connected)

total_connect = []
for node in range(1, node_max+1):
    connected = []
    if visited_bool[node] == False:
        DFS(node, visited_bool, connected)
        total_connect.append(connected)

print (len(total_connect))
