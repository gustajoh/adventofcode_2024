
def solution(input):
    
    score = 0
    with open(input) as file:
        for line in file:
            level = [int(x) for x in line.split()]
            res = checkValid(level)
            if not res:
                res2 = extraCheck(level)
            score += 1 if (res or res2) else 0
        
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

def extraCheck(level):
    print("CHECKING", level)
    for index in range (0,len(level)):
        if checkValid(remove_el(level,index)):
            return True
        
# def checkValid(array, depth):
    
#     ascending = array[0] < array[1]
#     for index in range(1,len(array)):
#         diff = abs(array[index-1] - array[index])
#         if (diff != 0 and diff < 4) and ((ascending and array[index-1] < array[index]) or (not ascending and array[index-1] > array[index])):
#             continue
#         else:
#             if depth == 0:
#                 return checkValid(remove_el(array, index-1),1 ) or checkValid(remove_el(array, index), 1)
#             else:
#                 return False
#     return True
        
def remove_el(list, index):
    return list[:index] + list[index+1:]

solution('input.txt')