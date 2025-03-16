from collections import deque
from collections import defaultdict

f = open('rosalind_scc.txt', 'r')
data = f.readlines()

def graph(data):
    edges = []
    max_node = list(map(int, data[0].strip().split(' ')))[0]
    #edge_num = list(map(int, data[0].strip().split(' ')))[1]
    for line in data[1:]:
        edges.append(list(map(int, line.strip().split(' '))))

    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
    return max_node, graph

max_node, graph = graph(data)


index = 0                        #node_id에 부여될 index이며 탐색시 +1 된다
node_id = [0] * (max_node + 1)   #각 node 에 부여된 id이다. 탐색한 순서와 같다
finished = [0] * (max_node + 1)  #node가 scc로 처리되었는지의 여부를 표시한다. 0 혹은 1 이다
scc_stack = deque()
scc_s = []

def SCC (start_node, graph):
    global index
    index += 1                              #우선 scc에 들어오면 index에 1을 더한다
    low_link = node_id[start_node] = index  #low link와 node id는 처음에 같은 값을 가지며, 그 값은 index이다 (탐색 순서). low_link는 start_node의 부모를 나타낸다
    scc_stack.append(start_node)            #stack에 본인을 넣는다

    for arr_node in graph[start_node]:                     #여기서 본인과 연결된 모든 node에 대해 탐색이 끝나지 않으면, 아래 finished를 조작하는 부분으로 넘어가지 않는다.
        if node_id[arr_node] == 0:                         #본인과 연결된 arr_node중, 아직 탐색되지 않은 node가 있다면
            low_link = min(low_link, SCC(arr_node, graph)) #본인의 low_link를 기존의 것 vs arr_node의 low_link중 작은 값으로 업데이트 한다 -> 만약 이후 경로에 사이클이 존재해, 사이클의 마지막 원소로부터 사이클의 시작id가 거슬러오고 있다면, 여기서 본인의 low_link도 사이클의 시작 원소의 id가 된다. 만약 이후 사이클이 없는 닫힌 경로가 있다면, 여기서 본인의 low_link는 유지된다.
        elif finished[arr_node] == 0:                      #node_id[arr_node] != 0이며 finished[arr_node] == 0 인 경우, 이미 방문 한 node 지만 scc 로 처리가 되지 않았다는 뜻 = 사이클 발견
            low_link = min(low_link, node_id[arr_node])    #사이클을 발견한 경우, 본인의 부모는 자동적으로 사이클의 시작점 (arr_node)의 id가 된다. 사이클의 경우 직관적으로, 시작 원소의 id가 항상 본인의 low_link보다 작아야 하는 것 같지만 반례가 존재하기 때문에 여기서도 min()을 통해 처리한다 -> 반례: 만약 본인에서 시작하는 또 다른 사이클이 지금 찾아낸 사이클이 들어오는 방향으로 뻗어나간다면, 방문 처리는 되었지만 finished 처리가 되지 않은 arr_node로 다시 뻗어나가면서 여기 elif문에 걸리며 본인의 low_link를 다른 값으로 덮어씌우게 됨

    if low_link == node_id[start_node]:  #만약 본인의 low_link값이 처음과 변하지 않았다면, 본인이 사이클의 부모가 된다 (cycle이 없는 경우, 그 path의 모든 node는 이런 형태를 띄며 그것은 각각이 길이 1짜리인 scc이다)
        scc_components = []
        while scc_stack:
            v = scc_stack.pop()
            scc_components.append(v)
            finished[v] = 1
            if start_node == v:          #stack에서 본인이 나올때까지 뽑아서 components에 넣는다.
                break
        scc_s.append(scc_components)

    return low_link  #함수 끝에서, SCC는 본인의 low link를 반환한다.

for i in range(1, max_node+1):
    if finished[i] == 0:
        SCC(i, graph)
print (len(scc_s))