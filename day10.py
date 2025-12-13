with open('input10.txt') as f:
    ans = 0

    for line in f.readlines():
        pieces = [x.strip() for x in line.split(" ")][:-1]
        board, buttons = pieces[0][1:-1], [[int(y) for y in x[1:-1].split(",")] for x in pieces[1:]]
        min_iter = {"val": float("inf")}

        def backtrack(cur_board, wanted_board, buttons, max_iter = 6, iter = 0):
            if cur_board == wanted_board:
                min_iter["val"] = min(min_iter["val"], iter)
                return
            if iter == max_iter or iter > min_iter["val"]: 
                return
            
            for b in buttons:
                new_board = [x for x in cur_board]
                for switch in b:
                    cur_val = new_board[switch]
                    if cur_val == ".":
                        new_board[switch] = "#"
                    else:
                        new_board[switch] = "."
                if iter + 1 < min_iter["val"]:
                    backtrack(new_board, wanted_board, buttons, max_iter, iter + 1)

        backtrack(["."] * len(board), [x for x in board], buttons)

        if min_iter["val"] > 1000:
            # Allow more combinations if the minimum is still not found
            backtrack(["."] * len(board), [x for x in board], buttons, 9)

        ans += min_iter["val"]

    print(ans)