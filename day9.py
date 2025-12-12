with open('input9.txt') as f:
    corners = [tuple(map(int, line.split(","))) for line in f]
    n = len(corners)

    def on_same_line(p1, p2):
        return p1[0] == p2[0] or p1[1] == p2[1]

    def area(p1, p2):
        return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

    border = set()
    global_max_x, global_max_y = -1, -1
    global_min_x, global_min_y = float("inf"), float("inf")

    def add_points_between(p1, p2):
        if p1[0] == p2[0]:
            y1, y2 = sorted([p1[1], p2[1]])
            for y in range(y1, y2 + 1):
                border.add((p1[0], y))
        else:
            x1, x2 = sorted([p1[0], p2[0]])
            for x in range(x1, x2 + 1):
                border.add((x, p1[1]))

    for i in range(n):
        p1 = corners[i]
        p2 = corners[(i + 1) % n]

        global_max_x = max(global_max_x, p1[0], p2[0])
        global_max_y = max(global_max_y, p1[1], p2[1])
        global_min_x = min(global_min_x, p1[0], p2[0])
        global_min_y = min(global_min_y, p1[1], p2[1])

        if on_same_line(p1, p2):
            add_points_between(p1, p2)

    def fill_polygon(corners):
        filled = set()
        ys = [y for _, y in corners]
        min_y = min(ys)
        max_y = max(ys)
        n = len(corners)

        for y in range(min_y, max_y + 1):
            xs = []
            print(y)
            for i in range(n):
                x1, y1 = corners[i]
                x2, y2 = corners[(i + 1) % n]

                # check if edge crosses this scanline
                if (y1 <= y < y2) or (y2 <= y < y1):
                    t = (y - y1) / (y2 - y1)
                    x = x1 + t * (x2 - x1)
                    xs.append(int(x))

            if not xs:
                continue

            xs.sort()

            # fill across pairs of intersections
            for i in range(0, len(xs), 2):
                x_start = xs[i]
                x_end = xs[i + 1]
                for x in range(x_start, x_end + 1):
                    filled.add((x, y))

        return filled

    interior = fill_polygon(corners)

    # merge border + interior
    new_points = list(interior.union(border))

    # ---------- Evaluate all rectangles from new_points ----------
    new_points_set = set(new_points)
    corners_set = set(corners)

    max_area = -1

    new_points_len = len(new_points)
    for i in range(new_points_len - 1):
        p1 = new_points[i]
        if p1 not in corners_set:
            continue

        for j in range(i + 1, new_points_len):
            p2 = new_points[j]
            if p2 not in corners_set:
                continue

            # axis-aligned rectangle formed by p1,p2 and 2 implied corners
            p3 = (p1[0], p2[1])
            p4 = (p2[0], p1[1])

            if p3 in new_points_set and p4 in new_points_set:
                max_area = max(max_area, area(p1, p2))

    print(max_area)