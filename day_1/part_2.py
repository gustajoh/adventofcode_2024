
def solution(input):
    left = []
    right = []
    with open(input) as file:
        for line in file:
            sp = line.split()
            left.append(int(sp[0]))
            right.append(int(sp[1]))
    
    my_dict = {}
    # Populate dict
    for number in left:
        count = 0
        if number not in my_dict.keys():
            for i in range(0,len(right)):
                if number == right[i]:
                    count += 1
            my_dict[number] = count
            
    score = 0
    for k,v in my_dict.items():
        score += k*v
    print(score)
    
solution('input.txt')