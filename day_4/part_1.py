import re

def main():
    with open('input.txt') as file:
        c = 0
        matrix = [list(line.strip()) for line in file]

        for i in range (0,len(matrix[0])):
            for j in range(0,len(matrix[1])):
                if matrix[i][j] == 'X':
                    c += explore(matrix, i, j)
        print(c)


def explore(m, i, j):
    norm = ['X', 'M', 'A', 'S']
    # up, down, left, right, and all diagonals
    paths = [1, 1, 1, 1, 1, 1, 1, 1]

    for step in range(1, 4):
        if paths[0] and not (checkbounds(m, i + step, j) and m[i + step][j] == norm[step]):
            paths[0] = 0
        if paths[1] and not (checkbounds(m, i - step, j) and m[i - step][j] == norm[step]):
            paths[1] = 0
        if paths[2] and not (checkbounds(m, i, j - step) and m[i][j - step] == norm[step]):
            paths[2] = 0
        if paths[3] and not (checkbounds(m, i, j + step) and m[i][j + step] == norm[step]):
            paths[3] = 0
        if paths[4] and not (checkbounds(m, i - step, j - step) and m[i - step][j - step] == norm[step]):
            paths[4] = 0
        if paths[5] and not (checkbounds(m, i + step, j - step) and m[i + step][j - step] == norm[step]):
            paths[5] = 0
        if paths[6] and not (checkbounds(m, i - step, j + step) and m[i - step][j + step] == norm[step]):
            paths[6] = 0
        if paths[7] and not (checkbounds(m, i + step, j + step) and m[i + step][j + step] == norm[step]):
            paths[7] = 0

    return sum(paths)




def checkbounds(m,i,j):
    return 0 <= i < len(m) and 0 <= j < len(m[0])
if __name__ == "__main__":
    main()