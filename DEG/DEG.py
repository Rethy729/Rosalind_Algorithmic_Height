data = open('rosalind_deg.txt', 'r')
rawdata = data.read()
rawdata_split = rawdata.split('\n')
edge = []

for pair in rawdata_split[:-1]:
    edge.append(list(map(int, pair.split(' '))))

node_max = edge[0][0]
edges = edge[1:]

graph = {}
for i in range(node_max):
    graph[i+1] = 0

for edge in edges:
        graph[edge[0]] += 1
        graph[edge[1]] += 1


count = []
for key in graph:
    count.append(graph[key])

text_file = open('output_deg.txt', 'w')
text_file.write(' '.join(map(str, count)))
text_file.close()
