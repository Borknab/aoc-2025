with open('input9.txt') as f:
    corners = [tuple([int(x) for x in line.split(",")]) for line in f.readlines()]
    n = len(corners)
    
    pairs = []
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            pairs.append([corners[i], corners[j]])

    def on_same_line(p1, p2):
        return p1[0] == p2[0] or p1[1] == p2[1]

    def area(p1, p2):
        return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

    points = set()

    global_max_x, global_max_y = -1, -1

    def add_points_between(p1, p2):
        if p1[0] == p2[0]:
            max_y = max(p1[1], p2[1])
            min_y = min(p1[1], p2[1])
            for y in range(min_y, max_y + 1):
                points.add((p1[0], y))
        else:
            max_x = max(p1[0], p2[0])
            min_x = min(p1[0], p2[0])
            for x in range(min_x, max_x + 1):
                points.add((x, p1[1]))

    def within(p, dir = None):
        if p[0] >= global_max_x + 2 or p[1] >= global_max_y + 2 or p[0] < 0 or p[1] < 0:
            return False
        if p in points:
            return True
        
        if dir == 1: return within((p[0] - 1, p[1]), 1) 
        elif dir == 2: return within((p[0], p[1] - 1), 2) 
        elif dir == 3: return within((p[0] + 1, p[1]), 3)
        elif dir == 4: return within((p[0], p[1] + 1), 4)
        else:
            return (
                within((p[0] - 1, p[1]), 1) and
                within((p[0], p[1] - 1), 2) and
                within((p[0] + 1, p[1]), 3) and
                within((p[0], p[1] + 1), 4)
            )

    for [p1, p2] in pairs:
        global_max_x = max(global_max_x, p1[0], p2[0])
        global_max_y = max(global_max_y, p1[1], p2[1])

        if on_same_line(p1, p2):
            add_points_between(p1, p2)

    new_points = []
    for i in range(global_max_y + 2):
        for j in range(global_max_x + 2):
            if within((j,i)) or (j, i) in points:
                new_points.append((j, i))

    new_pairs = []
    n1 = len(new_points)
    for i in range(0, n1 - 1):
        for j in range(i + 1, n1):
            new_pairs.append([new_points[i], new_points[j]])

    max_area = -1
    for [p1, p2] in new_pairs:
        # First check if the first 2 corners are within the ouline of the shape
        # Then check if the 2 other corners are within the area
        if ((p1 in corners) and
            (p2 in corners) and
            ((p1[0], p2[1]) in new_points and (p2[0], p1[1]) in new_points)
        ):
            max_area = max(max_area, area(p1, p2))
    print(max_area)