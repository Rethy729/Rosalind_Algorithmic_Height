import queue
from collections import defaultdict

f = open('rosalind_sdag.txt', 'r')
data = f.readlines()

def graph_gen(data):
    max_node = list(map(int, data[0].strip().split()))[0]
    edges = []
    for edge in data[1:]:
        edges.append(list(map(int, edge.strip().split())))

    graph = defaultdict(dict)
    graph_rev = defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
        graph_rev[edge[1]][edge[0]] = edge[2]
    return graph, graph_rev, max_node #{arr_node:{start_node:weight}}

DAG, DAG_rev, max_node= graph_gen(data)
#print (DAG)
#print (DAG_rev)

def incoming_degree_count(graphdata):
    node_set = set()
    for key in graphdata:
        node_set.add(key)
        for node in graphdata[key]:
            node_set.add(node)
    node_lst = list(node_set)
    IDC = [0] * (max(node_lst)+1)
    for key in graphdata:
        for arr_node in graphdata[key]:
            IDC[arr_node] += 1
    return IDC

IDC = incoming_degree_count(DAG)
#print (incoming_degree_count(DAG))

def khan(idc_lst, graphdata):
    dag_queue = queue.Queue()

    for i in range(len(idc_lst)): #appending the first idc == 0 nodes in dag_queue
        if idc_lst[i] == 0:
            dag_queue.put(i)

    topo_sort = []
    while len(topo_sort) != len(idc_lst): #next, until we get all the nodes in topo_sort
        node = dag_queue.get()
        topo_sort.append(node)
        if node in graphdata:
            for arr_node in graphdata[node]:
                idc_lst[arr_node] -= 1
                if idc_lst[arr_node] == 0:
                    dag_queue.put(arr_node)
        else:
            continue
    return topo_sort
topo_order = khan(IDC, DAG)

def DP(topo_order, graph_rev, max_node):
    #print (graph_rev)
    #print (topo_order)
    distance_lst = [99999999] * (max_node + 1)
    start_index = topo_order.index(1)
    distance_lst[1] = 0

    for i in range(start_index+1, max_node+1):
        distance = []
        for node in graph_rev[topo_order[i]]:
            if type(distance_lst[node]) == int:
                distance.append(distance_lst[node] + graph_rev[topo_order[i]][node])
        if distance == []:
            distance_lst[topo_order[i]] = 'x'
        else:
            distance_lst[topo_order[i]] = min(distance)

    for i, num in enumerate(distance_lst):
        if num == 99999999:
            distance_lst[i] = 'x'

    return distance_lst

print (' '.join(map(str, DP(topo_order, DAG_rev, max_node)[1:])))