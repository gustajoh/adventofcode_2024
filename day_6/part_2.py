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
    init_guard = guard
    direction = {
        '^': lambda x, y: (x-1, y),
        '>': lambda x, y: (x, y+1),
        'v': lambda x, y: (x+1, y),
        '<': lambda x, y: (x, y-1)
    }

    objs = set()
    objs.add(current)

    (d_i ,j_i) = direction[guard](*current)

    while(checkbounds(m, d_i, j_i)):
        if m[d_i][j_i] == '#':
            index += 1
            index %= 4
            guard = guards[index]
        else:  
            res = trywalk(m, (d_i, j_i), (i,j), guard, init_guard, guards, direction)
            if res[0]:
                objs.add(res[1])

            current = (d_i, j_i)
        (d_i, j_i) = direction[guard](*current)

    return len(objs)-1
    
def trywalk(m, curr, init, guard, init_guard, guards, direction):

    start = init
    in_vis = {}
    step = direction[guard](*curr)
    if not checkbounds(m, step[0], step[1]):
        return (False, (-1,-1))
    
    if m[step[0]][step[1]] != "#":
        new_obj = step
    elif m[step[0]][step[1]] == "#":
        new_obj = direction[guards[(guards.index(guard)+1) % 4]](*curr)

    current = start
    index = guards.index(init_guard)
    guard = init_guard
    (di, dj) = start

    while(checkbounds(m, di, dj)):
        m[new_obj[0]][new_obj[1]] = "O"
        if m[di][dj] == '#' or (di, dj) == new_obj:
            index += 1
            index %= 4
            guard = guards[index]
        else:
            if (di, dj) not in in_vis.keys():
                in_vis[(di, dj)] = [guard]
            elif guard in in_vis[(di, dj)]:
                return (True, new_obj)
            else:
                in_vis[(di, dj)].append(guard)

            
            current = (di, dj)
        (di, dj) = direction[guard](*current)
        
    return (False, None)

def checkbounds(m,i,j):
    return 0 <= i < len(m) and 0 <= j < len(m[0])

if __name__ == "__main__":
    main()