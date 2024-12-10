def main():
    with open("input.txt") as file:
        for line in file:
            drive = list(line.strip())

    b_i = 0
    block_list = []
    
    gaps = {}
    block_size = {}

    for i in range(len(drive)):
        if i % 2 == 0:
            block_size[str(b_i)] = int(drive[i])
            block_list.extend([str(b_i)] * int(drive[i]))
            b_i += 1
        else:
            gaps[len(block_list)] = int(drive[i])
            block_list.extend("." * int(drive[i]))

    for i in range(len(block_list)-1,-1,-1):
        if block_list[i] != "." and block_list[i] != "0":
            check_i = i
            curr = block_list[check_i]
            space = block_size[curr]
            gap_i, gap = check_gaps(block_size[curr], gaps)
            if (gap_i, gap) != (-1, -1) and gap_i < check_i:
                for j in range(block_size[curr]):
                    block_list[i-j], block_list[gap_i+j] = block_list[gap_i+j], block_list[i-j]

                del gaps[gap_i]
                gaps[gap_i+space] = gap-block_size[curr]
                gaps = dict(sorted(gaps.items()))

    checksum = 0
    for i in range(len(block_list)):
        if block_list[i] != ".":
            checksum += i*int(block_list[i])
            
    print(checksum)

def check_gaps(size, gaps):
    for k,v in gaps.items():
        if size <= v:
            return k, v
    return -1, -1

if __name__ == "__main__":
    main()