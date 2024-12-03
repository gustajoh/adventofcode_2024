import re

def solution(input):
    pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    sum = 0
    matches = []
    with open(input) as file:
        for line in file:
            matches.append(pattern.findall(line))

        for subarr in matches:
            for match in subarr:
                pair = match.replace("mul(",'').replace(")",'').split(",")
                print(pair)
                sum += int(pair[0])*int(pair[1])

        print(sum)            

solution('input.txt')