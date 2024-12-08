
def main():
    with open('input.txt') as file:
        matrix = [list(line.strip()) for line in file]
        
        antennas = {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                freq = matrix[i][j]
                if freq != ".":
                    if freq not in antennas.keys():
                        antennas[freq] = [(i,j)]
                    else:
                        antennas[freq].append((i,j))
                    
        
        a_nodes = set()
        transformations = [
            lambda x,y,xi,yi: (x+xi, y+yi),
            lambda x,y,xi,yi: (x-xi, y-yi),
            ]
        
        for p in antennas.values():
            for i in range(0,len(p)):
                for j in range(0,len(p)):
                    if i != j:
                        dist = (p[i][0] - p[j][0], p[i][1] - p[j][1])
                        trans_pos = [t(p[j][0], p[j][1], dist[0], dist[1]) for t in transformations]
                        
                        for p_t in trans_pos:
                            if p_t not in p and checkbounds(matrix,p_t):
                                a_nodes.add(p_t)
                        
        print(len(a_nodes))

def checkbounds(m, coords):
    return 0 <= coords[0] < len(m) and 0 <= coords[1] < len(m[0])
    
    
if __name__ == "__main__":
    main()