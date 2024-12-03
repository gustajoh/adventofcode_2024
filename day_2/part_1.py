
def solution(input):
    
    score = 0
    with open(input) as file:
        for line in file:
            level = [int(x) for x in line.split()]
            score += checkValid(level)
        
        print(score)
        
def checkValid(array):
    
    ascending = array[0] < array[1]
    for index in range(1,len(array)):
        diff = abs(array[index-1] - array[index])
        if (diff != 0 and diff < 4) and ((ascending and array[index-1] < array[index]) or (not ascending and array[index-1] > array[index]) ):
            continue
        else:
            return 0
    return 1
        

solution('input.txt')