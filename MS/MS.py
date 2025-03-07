data = open('rosalind_ms.txt', 'r')
rawdata_split = data.read().split("\n")
lst = list(map(int, rawdata_split[1].split(' ')))
n = int(rawdata_split[0])

def merge(array, start, mid, end):
    
    i = start
    j = mid
    temp_sort = []
    
    while i < mid and j < end:
        if array[i] > array[j]:
            temp_sort.append(array[j])
            j += 1
        else:
            temp_sort.append(array[i])
            i += 1
    temp_sort.extend(array[i:mid])
    temp_sort.extend(array[j:end])

    array[start:end] = temp_sort
    
def merge_sort(array, start, end):

    if start+1 == end:
        return
    
    mid = (start+end)//2
    
    merge_sort(array, start, mid)
    merge_sort(array, mid, end)

    merge(array, start, mid, end)
        
merge_sort(lst, 0,  n)

text_file = open('output_ms.txt', 'w')
text_file.write(" ".join(map(str, lst)))
text_file.close()
