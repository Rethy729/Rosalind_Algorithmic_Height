from collections import defaultdict
import queue

f = open('rosalind_hdag.txt', 'r')
data = f.read()
data_split = data[:-1].split('\n\n')

def graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
    return graph

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

def HP(ts, graph):
    i = 1
    start_node = ts[i]
    while True:
        if i < len(ts)-1 and ts[i+1] in graph[start_node]:
            i += 1
            start_node = ts[i]

        else:
            break
    if (i+1) != len(ts):
        return -1
    else:
        return 1

def data_processing(data):
    for chunk in data[1:]:
        edges = list(map(str, chunk.split('\n')))
        edges_data = []
        for edge in edges[1:]:
            edges_data.append(list(map(int, edge.split())))

        graph_data = graph(edges_data)
        #print (graph_data)
        IDC = incoming_degree_count(graph_data)
        #print (IDC)
        topo = khan(IDC, graph_data)
        #print (topo)
        contains_ham = HP(topo, graph_data)
        if contains_ham == 1:
            print (1, end = ' ')
            print (' '.join(map(str, topo[1:])))
        else:
            print (-1)
    #return answer

data_processing(data_split)