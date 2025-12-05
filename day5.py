with open('input5.txt') as f:
    # Step 1: merge the intervals
    intervals = []
    while f:
        line = f.readline()
        if len(line) < 3:
            break
        x, y = line.split("-")
        intervals.append([int(x), int(y)])
    intervals = list(sorted(intervals, key = lambda x: x[0]))
    merged_intervals = []
    cur_int = intervals[0]
    for [ifrom, ito] in intervals:
        if cur_int[1] >= ifrom:
            cur_int = [cur_int[0], max(ito, cur_int[1])]
        else:
            merged_intervals.append(cur_int)
            cur_int = [ifrom, ito]
    merged_intervals.append(cur_int)

    # Step 2: get the answer
    ans = 0
    for [ifrom, ito] in merged_intervals: ans += ito - ifrom + 1
    print(ans)