data = open('rosalind_ddeg.txt', 'r')
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

ddeg = []

for i in range(node_max):
    count = 0
    for nodes in graph[i+1]:
        count += len(graph[nodes])
    ddeg.append(count)

text_file = open('output_ddeg.txt', 'w')
text_file.write(' '.join(map(str, ddeg)))
text_file.close()

