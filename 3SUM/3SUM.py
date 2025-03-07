data = open('rosalind_3sum.txt', 'r')
rawdata = data.read()
rawdata_1 = rawdata.split('\n')
wholedata_str = rawdata_1[1:-1]

wholedata = []
for line in wholedata_str:
    wholedata.append([int(i) for i in line.split(' ')])

n = len(wholedata) #input line number
m = len(wholedata[0]) #input line length

for line in wholedata:

    indexed_line = []
    for i, num in enumerate(line):
        indexed_line.append((num, i+1))
    indexed_line.sort()
    
    three_index = []
    
    for i in range(m-2):
        
        left = i+1
        right = m-1

        if i >= 1 and indexed_line[i][0] == indexed_line[i-1][0]:
            continue

        while left < right:
            three_sum = indexed_line[i][0] + indexed_line[left][0] + indexed_line[right][0]

            if three_sum == 0:
                index = [indexed_line[right][1], indexed_line[left][1], indexed_line[i][1]]
                three_index.append(index)
                left += 1
                right -= 1

            elif three_sum < 0:
                left += 1
            
            elif three_sum > 0:
                right -= 1
    if len(three_index) == 0:
        print (-1)
        continue
    
    three_index.sort()
    three_index[0].sort()
    print (' '.join(map(str,three_index[0])))

    
                

