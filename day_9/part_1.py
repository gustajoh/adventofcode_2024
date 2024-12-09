def main():
    with open("input.txt") as file:
        for line in file:
            drive = list(line.strip())

    b_i = 0
    block_list = []
    for i in range(len(drive)):
        if i % 2 == 0:
            block_list.extend([str(b_i)] * int(drive[i]))
            b_i += 1
        else:
            block_list.extend("." * int(drive[i]))
    
    for i in range(len(block_list)):
        if block_list[i] == ".":
            last_i = len(block_list)-1
            while last_i > i and block_list[last_i] == ".":
                last_i -= 1
            
            if last_i <= i:
                break
            
            block_list[i], block_list[last_i] = block_list[last_i], block_list[i]
                
    checksum = 0
    for i in range(len(block_list)):
        if block_list[i] != ".":
            checksum += i*int(block_list[i])
            
    print(checksum)
    
if __name__ == "__main__":
    main()