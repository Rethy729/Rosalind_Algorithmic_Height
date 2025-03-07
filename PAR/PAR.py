data = open('rosalind_par.txt', 'r')
rawdata = data.read().split('\n')

n = int(rawdata[0])
lst = list(map(int, rawdata[1].split(' ')))


def pivot(lst, n):
    
    left = 1
    right = n-1
    pivot = lst[0]

    while left <= right:
        
        if lst[left] > pivot and lst[right] <= pivot:
            lst[left], lst[right] = lst[right], lst[left]
            
        if lst[left] <= pivot:
            left += 1
            
        if lst[right] > pivot: #when left = right, this if takes care of it
            right -= 1
            
    lst[0], lst[right] = lst[right], lst[0]
    
    return lst

answer = pivot(lst, n)
            
text_file = open('output_par.txt', 'w')
text_file.write(' '.join(map(str, answer)))
text_file.close()
