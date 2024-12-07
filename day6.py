# from collections import defaultdict
#
# with open("./sample/day6.txt", "r") as f:
#     result = 0
#     grid = []
#     temp = []
#     for line in f:
#         line = line.strip()
#         grid.append(line)
#         temp.append(list(line))
#
#     directions = [
#         (0, 1),
#         (1, 0),
#         (0, -1),
#         (-1, 0),
#     ]
#     turns = {
#         (0, 1): (1, 0),
#         (1, 0): (0, -1),
#         (0, -1): (-1, 0),
#         (-1, 0): (0, 1),
#     }
#     curDir = directions[3]
#     x = 0
#     y = 0
#     rows = len(grid)
#     cols = len(grid[0])
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == "^":
#                 x = i
#                 y = j
#     pos = set()
#     while True:
#         if 0 <= x < rows and 0 <= y < cols:
#             pos.add((x, y))
#             dx, dy = curDir
#
#             tx, ty = x, y
#             tx += dx
#             ty += dy
#
#             if 0 <= tx < rows and 0 <= ty < cols and grid[tx][ty] == "#":
#                 curDir = turns[curDir]
#             else:
#                 x, y = tx, ty
#         else:
#             break
#     print(result, len(pos))
#     print(len(pos))
#     for t in temp:
#         print("".join(t))
#
#         Part 2

with open("./sample/day6.txt", "r") as f:
    result = 0
    grid = []
    temp = []
    for line in f:
        line = line.strip()
        grid.append(list(line))
        temp.append(list(line))

    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]
    turns = {
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1),
    }
    x = 0
    y = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "^":
                x = i
                y = j
    pos = set()

    def goGoGo(x, y):
        curDir = directions[3]
        visited = set()
        while True:
            if 0 <= x < rows and 0 <= y < cols:
                posId = (x, y, curDir)
                if posId in visited:
                    return True
                visited.add(posId)
                pos.add((x, y))
                dx, dy = curDir

                tx, ty = x, y
                tx += dx
                ty += dy

                if 0 <= tx < rows and 0 <= ty < cols and grid[tx][ty] == "#":
                    curDir = turns[curDir]
                else:
                    x, y = tx, ty
            else:
                return False

    cur = 0
    total = rows * cols
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ".":
                grid[i][j] = "#"
                cur += 1
                print(f"{cur}/{total} -- {int((cur*100)/total)}% -- count: {result}")
                if goGoGo(x, y):
                    result += 1
                grid[i][j] = "."
    print(result, len(pos))
    print(len(pos))
    # for t in temp:
    #     print("".join(t))
