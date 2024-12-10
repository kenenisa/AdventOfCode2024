#
# # from collections import defaultdict
#
# with open("./sample/day10.txt", "r") as f:
#     result = 0
#     grid = []
#     for line in f:
#         line = line.strip()
#         grid.append(list(map(int, list(line))))
#
#     directions = [
#         (1, 0),
#         (-1, 0),
#         (0, 1),
#         (0, -1),
#     ]
#
#     rows = len(grid)
#     cols = len(grid[0])
#
#     def dfs(x, y, reachable):
#         if grid[x][y] == 9:
#             return reachable.add((x, y))
#         # ways = 0
#         for dx, dy in directions:
#             i = x + dx
#             j = y + dy
#             if 0 <= i < rows and 0 <= j < cols and grid[i][j] == grid[x][y] + 1:
#                 # ways += dfs(i, j)
#                 dfs(i, j, reachable)
#         # return ways
#
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == 0:
#                 uniqueHills = set()
#                 dfs(i, j, uniqueHills)
#                 result += len(uniqueHills)
#
#     print(result)
# from collections import defaultdict
#
# Part 2

with open("./sample/day10.txt", "r") as f:
    result = 0
    grid = []
    for line in f:
        line = line.strip()
        grid.append(list(map(int, list(line))))

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    rows = len(grid)
    cols = len(grid[0])

    def dfs(x, y):
        if grid[x][y] == 9:
            return 1
        ways = 0
        for dx, dy in directions:
            i = x + dx
            j = y + dy
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == grid[x][y] + 1:
                ways += dfs(i, j)
        return ways

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                result += dfs(i, j)

    print(result)
