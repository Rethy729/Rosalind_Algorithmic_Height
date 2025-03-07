data = open('rosalind_par3.txt', 'r')
rawdata = data.read().split('\n')

n = int(rawdata[0])
lst = list(map(int, rawdata[1].split(' ')))


def pivot_3(lst, n):
    
    left = 1
    right = n-1
    pivot = lst[0]

    while left <= right:
        
        if lst[left] > pivot and lst[right] <= pivot:
            lst[left], lst[right] = lst[right], lst[left]
            
        if lst[left] <= pivot:
            left += 1
            
        if lst[right] > pivot:
            right -= 1

    lst[0], lst[right] = lst[right], lst[0]

    distance = 0
    start = right
    while start >= 0:
        
        start -= 1

        if lst[start] == pivot:
            distance += 1
            lst[start], lst[right-distance] = lst[right-distance], lst[start]
    return lst

answer = pivot_3(lst, n)
            
text_file = open('output_par3.txt', 'w')
text_file.write(' '.join(map(str, answer)))
text_file.close()
