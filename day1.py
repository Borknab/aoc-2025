with open('input1.txt') as f:
    input = f.readlines()
    cur_position = 50
    ans = 0

    for line in input:
        direction = -1 if line[0] == 'L' else 1
        num_rotations = int(line[1:])
        old_position = cur_position
        cur_position += direction * num_rotations

        if cur_position > 99:
            ans += cur_position // 100
            cur_position = cur_position % 100
        elif cur_position <= 0:
            ans += (abs(cur_position) // 100) + 1 if old_position != 0 else (abs(cur_position) // 100)
            cur_position = 100 - abs(cur_position) % 100
            if cur_position == 100: cur_position = 0
        elif cur_position == 0:
            ans += 1

    print(ans)