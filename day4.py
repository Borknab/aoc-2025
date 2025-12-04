with open('input4.txt') as f:
    matrix = [l.strip() for l in f.readlines()]
    matrix_copy = [[x for x in line] for line in matrix]
    positions = [
        (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    n,m = len(matrix), len(matrix[0])
    accessible_points = 0

    while True:
        matrix = matrix_copy
        points_this_run = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "@":
                    num_rolls = 0
                    for x, y in positions:
                        new_i, new_j = i + x, j + y
                        if new_i < n and new_i >= 0 and new_j < m and new_j >= 0 and matrix[new_i][new_j] == "@":
                            num_rolls += 1
                    if num_rolls < 4:
                        points_this_run += 1
                        matrix_copy[i][j] = 'x'
        
        accessible_points += points_this_run
        if points_this_run == 0:
            break

    print(accessible_points)


