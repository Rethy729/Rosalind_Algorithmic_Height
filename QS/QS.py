data = open('rosalind_qs.txt', 'r')
rawdata = data.read().split('\n')

n = int(rawdata[0])
lst = list(map(int, rawdata[1].split(' ')))

def pivoting(lst, i, j): #i:start, j:end with 0_based index
    
    left = i+1
    right = j-1
    pivot = lst[i]

    while left <= right:
        
        if lst[left] > pivot and lst[right] <= pivot:
            lst[left], lst[right] = lst[right], lst[left]
        if lst[left] <= pivot:
            left += 1
        if lst[right] > pivot:
            right -= 1
                    
    lst[i], lst[right] = lst[right], lst[i]

    return right

def quick_sort(lst, start, end):
    
    if start < end:
        pivot_2 = pivoting(lst, start, end)
        quick_sort(lst, start, pivot_2)
        quick_sort(lst, pivot_2+1, end)
        
    return

quick_sort(lst, 0, n)

text_file = open('output.qs.txt', 'w')
text_file.write(' '.join(map(str, lst)))
text_file.close()

