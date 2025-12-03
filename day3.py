with open('input3.txt') as f:
    input = [l.strip() for l in f.readlines()]
    total = 0
    
    def max_number(line, start_idx, elems_left):
        n = len(line)
        max_elem, max_idx = -1, -1

        for i in range(start_idx, n):
            cur_elem = int(line[i])
            if i + elems_left < n:
                if cur_elem > max_elem:
                    max_elem, max_idx = cur_elem, i
            else:
                break
        
        return max_idx, f"{max_elem}"

    for line in input: 
        start_idx = 0
        max_capacity = ""
        for i in range(11, -1, -1):
            start_idx, max_n = max_number(line, start_idx, i)
            start_idx += 1
            max_capacity += max_n
        total += int(max_capacity)

    print(total)

