from collections import defaultdict

with open('input7.txt') as f:
    input = f.readlines()
    n, m = len(input), len(input[0])

    for i in range(m):
        if input[0][i] == "S": 
            xstart, ystart = [0, i]
            break

    visited = set()
    paths_for_node = defaultdict(int)
    def dfs(x, y, path):
        if (x, y) in visited:
            for node in path:
                paths_for_node[node] += paths_for_node[(x, y)]
            return paths_for_node[(x, y)]
        if x >= n or y >= m:
            path.append((x, y))
            for node in path:
                paths_for_node[node] += 1
            path.pop(-1)
            return 1

        visited.add((x, y))
        path.append((x, y))

        if input[x][y] == "^":
            res_left = dfs(x, y - 1, path) 
            res_right = dfs(x, y + 1, path)
            path.pop(-1)
            return res_left + res_right
        
        res = dfs(x + 1, y, path)
        path.pop(-1)

        return res

    print(dfs(xstart, ystart, []))