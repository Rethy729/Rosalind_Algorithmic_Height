data = open('rosalind_hea.txt', 'r')
rawdata = data.read().split('\n')
length = int(rawdata[0])
lst = list(map(int, rawdata[1].split(' ')))

def heapify(lst, length, idx): #this idx is 1-based
    
    largest = idx
    left = 2 * idx
    right = 2 * idx +1

    if left <= length and lst[left-1] > lst[largest-1]:
        largest = left
        
    if right <= length and lst[right-1] > lst[largest-1]:
        largest = right

    if largest != idx:
        lst[idx-1], lst[largest-1] = lst[largest-1], lst[idx-1]
        
        heapify(lst, length, largest) #if switching happens, again make a heap tree with a top-node "largest" 

for i in range(length//2, 0, -1): #start from the lowest "parent" node, down-to-up.
    heapify(lst, length, i)

text_file = open('output_hea.txt', 'w')
text_file.write((" ".join(map(str, lst))))
text_file.close()
