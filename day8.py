# #
# # from collections import defaultdict
#
# from collections import defaultdict
#
#
# with open("./sample/day8.txt", "r") as f:
#     result = 0
#     grid = []
#     for line in f:
#         line = line.strip()
#         grid.append(list(line))
#     rows = len(grid)
#     cols = len(grid[0])
#     antinodes = set()
#     directions = [
#         (1, 0),
#         (-1, 0),
#         (1, 1),
#         (-1, -1),
#         (0, 1),
#         (0, -1),
#         (1, -1),
#         (-1, 1),
#     ]
#
#     def goGoGo(values):
#         for x, y in values:
#             for i, j in values:
#                 if x != i and y != j:
#                     rowDiff = x - i
#                     colDiff = y - j
#                     firstNode = (x + rowDiff, y + colDiff)
#                     secondNode = (i - rowDiff, j - colDiff)
#                     fx, fy = firstNode
#                     sx, sy = secondNode
#                     if 0 <= fx < rows and 0 <= fy < cols:
#                         antinodes.add(firstNode)
#                     if 0 <= sx < rows and 0 <= sy < cols:
#                         antinodes.add(secondNode)
#
#     nodes = defaultdict(list)
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] != ".":
#                 nodes[grid[i][j]].append((i, j))
#     for key, values in nodes.items():
#         goGoGo(values)
#     for row in grid:
#         print(row)
#     print(result, len(antinodes))
# from collections import defaultdict
#
# Part 2

from collections import defaultdict


with open("./sample/day8.txt", "r") as f:
    result = 0
    grid = []
    for line in f:
        line = line.strip()
        grid.append(list(line))
    rows = len(grid)
    cols = len(grid[0])
    antinodes = set()
    directions = [
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (0, 1),
        (0, -1),
        (1, -1),
        (-1, 1),
    ]

    def goGoGo(values):
        for x, y in values:
            for i, j in values:
                if x != i and y != j:
                    antinodes.add((x, y))
                    antinodes.add((i, j))
                    rowDiff = x - i
                    colDiff = y - j
                    firstNode = (x + rowDiff, y + colDiff)
                    secondNode = (i - rowDiff, j - colDiff)
                    fx, fy = firstNode
                    sx, sy = secondNode
                    while 0 <= fx < rows and 0 <= fy < cols:
                        antinodes.add((fx, fy))
                        fx += rowDiff
                        fy += colDiff
                    while 0 <= sx < rows and 0 <= sy < cols:
                        antinodes.add((sx, sy))
                        sx -= rowDiff
                        sy -= colDiff

    nodes = defaultdict(list)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != ".":
                nodes[grid[i][j]].append((i, j))
    for key, values in nodes.items():
        goGoGo(values)
    for row in grid:
        print(row)
    print(result, len(antinodes))
