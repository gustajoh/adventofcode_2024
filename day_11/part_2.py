def main():
    stones = {}

    with open('input.txt') as file:
        init = file.readline().split(" ")
    
    for s in init:
        stones[int(s)] = 1
    first = ""
    second = ""
    for _ in range(150):
        cp = {}
        for stone, count in list(stones.items()):
            l = len(str(stone))
            if l % 2 == 0:
                first = stone // 10**(len(str(stone)) // 2)
                second = stone % 10**(len(str(stone)) // 2)
                
                cp[first] = cp.get(first, 0) + count
                cp[second] = cp.get(second, 0) + count
            elif stone == 0:
                cp[1] = cp.get(1, 0) + count
            else:
                mult = stone*2024
                cp[mult] = cp.get(mult, 0) + count
        stones = cp

    sum = 0
    for k,v in stones.items():
        if v > 0:
            sum += v
    print(sum)

main()