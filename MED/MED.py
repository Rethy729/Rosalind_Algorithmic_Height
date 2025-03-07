data = open('rosalind_med.txt', 'r')
rawdata = data.read().split('\n')

n = int(rawdata[0])
lst = list(map(int, rawdata[1].split(' ')))
k = int(rawdata[2])

def median(lst, k):
    
    left = 1
    right = len(lst)-1
    pivot = lst[0]

    while left <= right:
        
        if lst[left] > pivot and lst[right] <= pivot:
            lst[left], lst[right] = lst[right], lst[left]
        if lst[left] <= pivot:
            left += 1
        if lst[right] > pivot:
            right -= 1
                    
    lst[0], lst[right] = lst[right], lst[0]

    if right == k-1: #0_based_index(right), 1_based_index(k)
        return lst[right]

    elif right > k-1:
        return median(lst[:right], k)

    else:
        return median(lst[right+1:], k-(right+1))

print (median(lst, k))