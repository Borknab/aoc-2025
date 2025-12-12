from collections import defaultdict

graph = defaultdict(list)

with open('input11.txt') as f:
    for line in f.readlines():
        src, dest = line.split(":")
        dest_nodes = dest.strip().split(" ")
        for node in dest_nodes:
            graph[src].append(node)

mem = {}

def count_paths(cur, target):
    if (cur, target) in mem:
        return mem[(cur, target)]

    if cur == target:
        return 1
    
    total = 0
    for child in graph[cur]:
        total += count_paths(child, target)

    mem[(cur, target)] = total

    return total

paths_1 = (count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out"))
paths_2 = (count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out"))

print(paths_1 + paths_2)