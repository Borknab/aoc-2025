from collections import defaultdict

with open('input6.txt') as f:
    input = f.readlines()
    nums = []
    operations = []

    for i in range(len(input[0])):
        nums_cur = []
        for j in range(len(input) - 1):
            nums_cur.append(input[j][i])
        nums.append(nums_cur)

    cur_nums = []
    new_nums = []
    for cnums in nums:
        if cnums in [[' ', ' ', ' ', ' '], ['\n', '\n', '\n', '\n']]:
            new_nums.append(cur_nums)
            cur_nums = []
        else:
            cur_nums.append(cnums)

    for i in range(len(input[-1])):
        el = input[-1][i]
        if el != ' ': operations.append(el)

    ans = 0
    for i in range(len(new_nums)):
        op = operations[i]
        cnums = new_nums[i]
        real_nums = []
        for k in cnums:
            ckey = 1
            kreal = ""
            for k1 in k: 
                if k1 != " ":
                    kreal += k1
            real_nums.append(int(kreal))

        if op == "*":
           cans = 1
           for on in real_nums:
               cans *= on 
           ans += cans
        if op == "+":
           cans = 0
           for on in real_nums:
               cans += on 
           ans += cans

    print(ans)