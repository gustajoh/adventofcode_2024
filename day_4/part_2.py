def main():
    with open('input.txt') as file:
        c = 0
        matrix = [list(line.strip()) for line in file]

        for i in range (0,len(matrix[0])):
            for j in range(0,len(matrix[1])):
                if matrix[i][j] == 'A':
                    c += explore(matrix, i, j)
        print(c)


def explore(m, i, j):
    if not(checkbounds(m,i-1,j-1) and checkbounds(m,i-1,j+1) and checkbounds(m,i+1,j+1) and checkbounds(m,i+1,j-1)):
        return 0

    upleft = m[i-1][j-1]
    upright = m[i-1][j+1]
    downleft = m[i+1][j-1]
    downright = m[i+1][j+1]
    
    if ((upleft == "M" and downright == "S") or (upleft=="S" and downright == "M")) and ((upright == "S" and downleft == "M") or (upright == "M" and downleft == "S")):
            return 1
            
        
    return 0

def checkbounds(m,i,j):
    return 0 <= i < len(m) and 0 <= j < len(m[0])

if __name__ == "__main__":
    main()