#For every merge sort, the sum of the index difference before&after = total inversion

data = open('rosalind_inv.txt', 'r')
rawdata_split = data.read().split("\n")
lst = list(map(int, rawdata_split[1].split(' ')))
n = int(rawdata_split[0])
inversion_count = 0

def merge(array, start, mid, end):
    global inversion_count
    i = start
    j = mid
    temp_sort = []
    
    while i < mid and j < end:
        if array[i] > array[j]:
            temp_sort.append(array[j])
            if j - (start+len(temp_sort)-1) > 0:
                inversion_count += (j - (start+len(temp_sort)-1))
            j += 1
        else:
            temp_sort.append(array[i])
            if i - (start+len(temp_sort)-1) > 0:
                inversion_count += (i - start+len(temp_sort)-1)
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

print (inversion_count)
