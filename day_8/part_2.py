
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
        transformation = lambda x,y,xi,yi: (x+xi, y+yi)  
        
        for p in antennas.values():
            for i in range(0,len(p)):
                for j in range(0,len(p)):
                    if i != j:
                        dist = (p[i][0] - p[j][0], p[i][1] - p[j][1])
                        d_i, d_j = p[j][0], p[j][1]
                        trans_pos = []
                        while(checkbounds(matrix, d_i, d_j)):
                            trans_pos.append((d_i, d_j))
                            (d_i, d_j) = transformation(d_i, d_j, dist[0], dist[1])
                                                    
                        for p_t in trans_pos:
                            a_nodes.add(p_t)
                            
                            # for checking output
                            if matrix[p_t[0]][p_t[1]] == ".":
                                matrix[p_t[0]][p_t[1]] = "#"
                        
        print(len(a_nodes))
        with open("out.txt", "w") as file:
            for row in matrix:
                file.write("".join(map(str, row)) + "\n")

def checkbounds(m, i, j):
    return 0 <= i < len(m) and 0 <= j < len(m[0])
    
    
if __name__ == "__main__":
    main()