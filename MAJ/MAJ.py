data = open('rosalind_maj.txt', 'r')
rawdata = data.read()
rawdata_split = rawdata.split("\n")
data = []

for string in rawdata_split[:-1]:
    lst = [int(i) for i in string.split(' ')]
    data.append(lst)

line_num = data[0][0]
line_length = data[0][1]

def threshold(n):
    if n%2 == 0:
        threshold = n/2
    if n%2 == 1:
        threshold = n/2 +1
    return threshold

def majority(data, threshold):
    
    majority = [0] * line_num
    
    for i, line in enumerate(data):
        for element in set(line):
            count = 0
            for num in line:
                if element == num:
                    count += 1
            if count > threshold:
                majority[i] = element
                break
            else:
                majority[i] = -1

    return majority
    
threshold = threshold(line_length)
print (' '.join(map(str, majority(data[1:], threshold))))
