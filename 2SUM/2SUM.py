data = open('rosalind_2sum.txt', 'r')
rawdata = data.read()
rawdata_1 = rawdata.split('\n')
wholedata = rawdata_1[1:-1]

wholedata_1 = []
for line in wholedata:
    wholedata_1.append([int(i) for i in line.split(' ')])

n = len(wholedata_1) #input line number
m = len(wholedata_1[0]) #input line length


for line in wholedata_1:
    count = 0
    q = m
    p = 0
    for i in range(m):
        if (-line[i]) in line[i+1:]:
            if q > (line[i+1:].index(-line[i])+i+1):
                q = (line[i+1:].index(-line[i])+i+1)
                p = i
                
            count += 1    
    if count == 0:
        print (-1)
    else:
        print (p+1, q+1)

