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

    (d_i ,j_i) = direction[guard](*current)
    count = 0
    distinct = set()

    while(checkbounds(m, d_i, j_i)):
        if m[d_i][j_i] == '#':
            index += 1
            index %= 4
            guard = guards[index]
        else:
            if (d_i,j_i) not in distinct:
                count += 1
                distinct.add((d_i, j_i))
            current = (d_i, j_i)
        (d_i ,j_i) = direction[guard](*current)
    return count
    
def checkbounds(m,i,j):
    return 0 <= i < len(m) and 0 <= j < len(m[0])

if __name__ == "__main__":
    main()