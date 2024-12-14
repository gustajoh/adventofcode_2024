import re
def main():
    a_buttons = []
    b_buttons = []
    prizes = []
    index = 0
    with open('input.txt') as file:
        for line in file:
            if line.strip() == "":
                continue
            if index == 0:                
                line = re.sub(r"[^0-9,]+", "", line).split(',')
                a_buttons.append((int(line[0]), int(line[1])))
            elif index == 1:
                line = re.sub(r"[^0-9,]+", "", line).split(',')
                b_buttons.append((int(line[0]), int(line[1])))
            elif index == 2:
                line = re.sub(r"[^0-9,]+", "", line).split(',')
                prizes.append((int(line[0]), int(line[1])))
 
            index = (index + 1) % 3
    
        c = 0
        for i in range(len(prizes)):
            x1 = a_buttons[i][0]
            y1 = a_buttons[i][1]

            x2 = b_buttons[i][0]
            y2 = b_buttons[i][1]

            prize = prizes[i]
            res = solve(x1, x2, y1, y2, prize)
            c += res

    print(c)

def solve(x1, x2, y1, y2, prize):
    limit = prize[0]//x1 + 1
    mul = 0
    mul2 = 0
    solutions = []

    while mul < limit:
        mul += 1
        if (prize[0] - (x1*mul)) % x2 == 0:
            mul2 = int((prize[0] - (x1*mul)) / x2)
            if y1*mul + y2*mul2 == prize[1]:
                solutions.append(mul*3 + mul2)

    if solutions == []:
        return 0
    return min(solutions)

main()