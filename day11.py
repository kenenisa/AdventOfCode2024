# from collections import defaultdict

with open("./sample/day11.txt", "r") as f:
    result = 0
    stones = []
    for line in f:
        line = line.strip()
        stones = list(map(int, line.split()))

    blinks = 75
    memo = {}

    def dfs(num, step) -> int:
        if step == 0:
            return 1
        if (num, step) in memo:
            return memo[(num, step)]
        count = 0

        if num == 0:
            count += dfs(1, step - 1)
        elif len(str(num)) % 2 == 0:
            s = str(num)
            count += dfs(int(s[: len(s) // 2]), step - 1)
            count += dfs(int(s[len(s) // 2 :]), step - 1)
        else:
            count += dfs(num * 2024, step - 1)
        memo[(num, step)] = count
        return count

    for i in stones:
        print("Solved", i)
        result += dfs(i, blinks)
    print(result)
    #
    # for _ in range(blinks):
    #     i = 0
    #     newStones = []
    #     for i in range(len(stones)):
    #         if stones[i] == 0:
    #             newStones.append(1)
    #         elif len(str(stones[i])) % 2 == 0:
    #             s = str(stones[i])
    #             newStones.append(int(s[: len(s) // 2]))
    #             newStones.append(int(s[len(s) // 2 :]))
    #         else:
    #             stones[i] *= 2024
    #             newStones.append(stones[i] * 2024)
    #     stones = newStones
    #     print(_, len(stones))
    # print(len(stones))
