from collections import defaultdict

with open('input2.txt') as f:
    input = f.readlines()
    nums = defaultdict(int)
    ans = 0

    def invalid_id(x):
        s = str(x)
        if len(s) % 2 != 0: return False
        mid = len(s) // 2
        return s[:mid] == s[mid:]

    def invalid_id_pt2(x):
        s = str(x)
        n = len(s)
        ans = False

        for patch_length in range(len(s) // 2, 0, -1):
            if (n % patch_length == 0):
                num_times = n // patch_length
                all_equal = True
                
                for i in range(num_times):
                    if s[i*patch_length : (i + 1) * patch_length] != s[:patch_length]:
                        all_equal = False
                        break

                if all_equal: 
                    ans = True
                    break

        return ans

    for line in input:
        for pair in line.split(","):
            if len(pair) > 2:
                [x, y] = [int(e) for e in pair.split("-")]
                for num in range(x, y + 1):
                    nums[num] += 1

    for num in nums:
        if invalid_id_pt2(num):
            ans += num

    print(ans)