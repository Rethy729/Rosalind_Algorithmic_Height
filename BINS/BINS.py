data = open('rosalind_bins.txt', 'r')
rawdata = data.read()
rawdata_split = rawdata.split("\n")
array_string = rawdata_split[2]
keys_string = rawdata_split[3]

array_list = list(map(int, array_string.split(' ')))
keys_list = list(map(int, keys_string.split(' ')))

def binary_search(array_list, key): #Binary search function
    start = 0                       #0_based indexing
    end = len(array_list)-1 

    while start <= end:             #binary search
        mid = (start + end) // 2

        if array_list[mid] == key:
            return mid+1

        elif array_list[mid] > key:
            end = mid-1

        else:
            start = mid+1

    return -1                       #returns -1 if key matches nothing in array_list

output = []

for key in keys_list:
    output.append(binary_search(array_list, key))

text_file = open('output_bins.txt', 'w')
text_file.write((" ".join(map(str, output))))
text_file.close()
    
