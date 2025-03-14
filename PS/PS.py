data = open('rosalind_ps.txt', 'r')
rawdata = data.read().split('\n')
lst = list(map(int, rawdata[1].split(' ')))
length_init = int(rawdata[0])
k = int(rawdata[2])

def heapify(lst, idx, maximum): #this idx is 1-based, maximum is the upper bound of childs (also 1_based)

    smallest = idx
    left = 2 * idx
    right = 2 * idx+1

    if left <= maximum and lst[left-1] < lst[smallest-1]:
        smallest = left
        
    if right <= maximum and lst[right-1] < lst[smallest-1]:
        smallest = right

    if smallest != idx:
        lst[idx-1], lst[smallest-1] = lst[smallest-1], lst[idx-1]
        
        heapify(lst, smallest, maximum) #if switching happens, again make a heap tree with a top-node "largest"

for i in range(length_init//2, 0, -1): #initial heapify
    heapify(lst, i, length_init)

lst_k = []
for n in range(length_init, length_init-k, -1):
    lst_k.append(lst[0])
    lst[0], lst[n-1] = lst[n-1], lst[0]
    heapify(lst, 1, n-1)

#make a reverse_heap, and do the heapify until the input k -> need to be modified

text_file = open('output_ps.txt', 'w')
text_file.write(' '.join(map(str, lst_k)))
text_file.close()
