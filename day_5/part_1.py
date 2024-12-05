import re
from collections import defaultdict

def main():
    pattern = re.compile(r"\d+\|\d+")

    rules = defaultdict(list)
    res = 0

    with open('input.txt') as file:
        for line in file:
            if pattern.match(line):
                split = line.strip().split("|")
                rules[split[0]].append(split[1])
            elif line != "\n":
                res += evalUpdate(line.strip().split(","), rules)
    print(res)

def evalUpdate(update, rules):
    for index in range(0,len(update)):
        curr = update[index]
        for rest in update[index+1:]:
            if rest not in rules[curr]:
                return 0
            
    return int(update[len(update)//2])

if __name__ == "__main__":
    main()