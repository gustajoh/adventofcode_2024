import re

def solution(input):
    sum = 0
    concatenated = ""
    with open(input) as file:
        for line in file:
            concatenated += line.strip()

    dos = concatenated.split("do()")
    for line in dos:
        donts = line.split("don't()")
        sum += calc(donts[0])
    print(sum)

def calc(line):
    pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    matches = pattern.findall(line)
    sum = 0
    for match in matches:
        pair = match.replace("mul(",'').replace(")",'').split(",")
        sum += int(pair[0])*int(pair[1])

    return sum

solution('input.txt')