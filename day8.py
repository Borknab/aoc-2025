from collections import Counter

with open('input8.txt') as f:
    input = [tuple([int(x) for x in line.split(",")]) for line in f.readlines()]
    n = len(input)

    def euclidean_distance(p, q):
        return (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2 + (q[2] - p[2]) ** 2
    
    
    pairs = []
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            pairs.append([input[i], input[j]])

    pairs.sort(key = lambda p: euclidean_distance(p[0], p[1]))

    junction_lkp = {}
    for point in input: junction_lkp[point] = 0

    junction_id = 1

    def all_values_equal(val_comp):
        for v in junction_lkp.values():
            if v != val_comp:
                return False
        return True

    for [x, y] in pairs:
        x_lkp = junction_lkp[x]
        y_lkp = junction_lkp[y]
        if x_lkp != 0 and x_lkp == y_lkp:
            # Part of the same juction, skip!
            pass
        elif x_lkp == 0 and y_lkp == 0:
            # Both nodes are not part of any junction
            junction_lkp[x] = junction_id
            junction_lkp[y] = junction_id
            junction_id += 1
        elif (x_lkp == 0 and y_lkp != 0) or (x_lkp != 0 and y_lkp == 0):
            # One node in no circuit, add it to an existing circuit
            if x_lkp == 0: junction_lkp[x] = y_lkp
            else: junction_lkp[y] = x_lkp
        else:
            # Different circuits, unite them
            max_lkp, min_lkp = max(x_lkp, y_lkp), min(x_lkp, y_lkp)
            for k in junction_lkp.keys():
                if junction_lkp[k] == min_lkp:
                    junction_lkp[k] = max_lkp

        if junction_lkp[x] != 0 and all_values_equal(junction_lkp[x]):
            print(x[0] * y[0])
            break