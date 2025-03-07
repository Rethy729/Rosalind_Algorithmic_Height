data = open('rosalind_ins.txt', 'r')
rawdata = data.read().split('\n')
n = int(rawdata[0])
array = list(map(int, rawdata[1].split(' ')))

def insertion_Sort(array, n):
    
    count = 0
    
    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
                count += 1
            else:
                break

    return count

print (insertion_Sort(array, n))

