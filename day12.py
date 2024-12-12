# from collections import defaultdict

from collections import defaultdict


with open("./sample/day12.txt", "r") as f:
    result = 0
    grid = []
    for line in f:
        line = line.strip()
        grid.append(list(line))
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    regions = defaultdict(set)

    up = ("10", "-10")
    down = ("01", "0-1")

    sideDirection = {
        "10": [(0, 1), (0, -1)],
        "-10": [(0, 1), (0, -1)],
        "01": [(1, 0), (-1, 0)],
        "0-1": [(1, 0), (-1, 0)],
    }

    def dfs(i, j, parent):
        visited.add((i, j))

        a = 0
        for dx, dy in directions:
            x = i + dx
            y = j + dy

            if 0 <= x < rows and 0 <= y < cols:
                if (x, y) not in visited and grid[x][y] == grid[i][j]:
                    a += dfs(x, y, parent) + 1
            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != grid[i][j]:
                regions[parent].add((x, y, f"{dx}{dy}"))

        return a

    # while len(proccessed) < edges:

    parentAreaSet = defaultdict(int)
    parentList = []
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                parent = (i, j)
                a = dfs(i, j, parent)
                parentAreaSet[parent] = a + 1
                parentList.append(parent)

    processed = set()
    for parent, region in regions.items():
        tempSet = region.copy()
        for i, j, dir in region:
            # print("START: ", i, j)
            processed.add((i, j, dir))
            for dx, dy in sideDirection[dir]:
                x = i + dx
                y = j + dy
                # print("Dir switch: ", x, y)
                while (
                    (x, y, dir) in tempSet
                    and -1 <= x < rows + 1
                    and -1 <= y < cols + 1
                    and (x, y, dir) not in processed
                ):
                    # print("Removing: ", x, y, dir)
                    tempSet.remove((x, y, dir))
                    x += dx
                    y += dy
            # print("-----")

        regions[parent] = tempSet

    for parent in parentList:
        result += parentAreaSet[parent] * len(regions[parent])
        i, j = parent
        print(
            grid[i][j],
            parentAreaSet[parent],
            " * ",
            len(regions[parent]),
            " = ",
            parentAreaSet[parent] * len(regions[parent]),
        )

    print(result)
