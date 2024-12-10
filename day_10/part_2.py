def main():    
    with open('input.txt') as file:
        matrix = [[int(ch) for ch in row.strip()] for row in file]
    score = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                score += walk(matrix, i, j, 0)

    print(score)
def walk(m, i, j , curr):
    steps = peek(m, i, j, curr)

    if not steps:
        return 0
    
    if curr == 8:
        return len(steps)
    total = 0
    for (di, dj) in steps:
        total += walk(m,di,dj,curr+1)

    return total

def peek(m, i, j, curr):
    coords = []
    if checkbounds(m,i+1,j) and m[i+1][j] == curr+1:
        coords.append((i+1, j))

    if checkbounds(m,i-1,j) and m[i-1][j] == curr+1:
        coords.append((i-1, j))

    if checkbounds(m,i,j+1) and m[i][j+1] == curr+1:
        coords.append((i, j+1))

    if checkbounds(m,i,j-1) and m[i][j-1] == curr+1:
        coords.append((i, j-1))

    return coords



def checkbounds(m, i, j):
    return 0 <= i < len(m) and 0 <= j < len(m[i])

if __name__ == "__main__":
    main()