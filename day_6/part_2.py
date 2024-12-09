import numpy as np

def main():
    matrix = []
    with open('input.txt') as file:
        matrix = [list(line.strip()) for line in file]


    guards = ["<","^","v",">"]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):                
            if matrix[i][j] in guards:
                print(startgame(matrix, i, j, matrix[i][j]))

def startgame(m,i,j,guard):
    current = (i,j)
    guards = ["^",">","v","<"]
    index = guards.index(guard)
    direction = {
        '^': lambda x, y: (x-1, y),
        '>': lambda x, y: (x, y+1),
        'v': lambda x, y: (x+1, y),
        '<': lambda x, y: (x, y-1)
    }

    objs = set()
    objs.add(current)

    (d_i ,j_i) = direction[guard](*current)
    distinct = {}

    while(checkbounds(m, d_i, j_i)):
        if m[d_i][j_i] == '#':
            index += 1
            index %= 4
            guard = guards[index]
        else:
            if current in distinct.keys():
                if guards[(index+1)%4] == distinct[current] and direction[guard](*current) not in objs:
                    objs.add(direction[guard](*current))
            else:
                distinct[current] = guard
            current = (d_i, j_i)
        (d_i, j_i) = direction[guard](*current)
    return len(objs)-1
    
def checkbounds(m,i,j):
    return 0 <= i < len(m) and 0 <= j < len(m[0])

if __name__ == "__main__":
    main()