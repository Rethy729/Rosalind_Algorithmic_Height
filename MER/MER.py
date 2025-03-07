data = open('rosalind_mer.txt', 'r')
rawdata = data.read()
rawdata_split = rawdata.split("\n")

n = int(rawdata_split[0]) #length of array_A
m = int(rawdata_split[2]) #length of array_B

array_A = list(map(int, rawdata_split[1].split(' ')))
array_B = list(map(int, rawdata_split[3].split(' ')))

def merge(array_1, array_2):
    
    merge_sort = []
    i = 0
    j = 0
    while i < len(array_1) and j < len(array_2):
        if array_1[i] > array_2[j]:
            merge_sort.append(array_2[j])
            j += 1            
        else:
            merge_sort.append(array_1[i])
            i += 1

    merge_sort.extend(array_1[i:])
    merge_sort.extend(array_2[j:])
    
    return merge_sort

answer = merge(array_A, array_B)

text_file = open('output.txt', 'w')
text_file.write(" ".join(map(str, answer)))
text_file.close()

