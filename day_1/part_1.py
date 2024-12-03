

def solution(input):
    left = []
    right = []
    with open(input) as file:
        for line in file:
            sp = line.split()
            left.append(int(sp[0]))
            right.append(int(sp[1]))
    left.sort()
    right.sort()
    
    dist = 0
    for index in range(0,len(left)):
        dist += abs(left[index] - right[index])
        
    print(dist)
        
solution('input.txt')
