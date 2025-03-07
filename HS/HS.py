data = open('rosalind_hs.txt', 'r')
rawdata = data.read().split('\n')
lst = list(map(int, rawdata[1].split(' ')))
length_init = int(rawdata[0])

def heapify(lst, idx, maximum): #this idx is 1-based, maximum is the upper bound of childs (also 1_based)

    largest = idx
    left = 2 * idx
    right = 2 * idx +1

    if left <= maximum and lst[left-1] > lst[largest-1]:
        largest = left
        
    if right <= maximum and lst[right-1] > lst[largest-1]:
        largest = right

    if largest != idx:
        lst[idx-1], lst[largest-1] = lst[largest-1], lst[idx-1]
        
        heapify(lst, largest, maximum) #if switching happens, again make a heap tree with a top-node "largest" 

for i in range(length_init//2, 0, -1): #initial heapify
    heapify(lst, i, length_init)

for n in range(length_init, 0, -1):
    
    lst[0], lst[n-1] = lst[n-1], lst[0] #change HEAD and TAIL
    heapify(lst, 1, n-1)            #re-heapify starting from the HEAD

text_file = open('output_hs.txt', 'w')
text_file.write(' '.join(map(str, lst)))
text_file.close()
