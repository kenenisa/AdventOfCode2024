# # from collections import defaultdict
#
# with open("./sample/day4.txt", "r") as f:
#     result = 0
#     all = []
#     for line in f:
#         line = line.strip()
#         all.append(line)
#
#     rows = len(all)
#     cols = len(all[0])
#
#     def search(i, j):
#         directions = [
#             (0, 1),
#             (1, 1),
#             (1, 0),
#             (1, -1),
#             (0, -1),
#             (-1, -1),
#             (-1, 0),
#             (-1, 1),
#         ]
#         count = 0
#         for dx, dy in directions:
#             x, y = i, j
#             s = ""
#             while len(s) < 4 and 0 <= x < rows and 0 <= y < cols:
#                 s += all[x][y]
#                 x += dx
#                 y += dy
#             if s == "XMAS":
#                 count += 1
#         return count
#
#     for row in range((len(all))):
#         for col in range(len(all[row])):
#             if all[row][col] == "X":
#                 result += search(row, col)
#
#     print(result)


# Part 2

with open("./sample/day4.txt", "r") as f:
    result = 0
    all = []
    for line in f:
        line = line.strip()
        all.append(line)

    rows = len(all)
    cols = len(all[0])

    def search(i, j):
        directions = [
            (-1, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
        ]
        s = ""
        for dx, dy in directions:
            x, y = i, j
            x += dx
            y += dy
            if 0 <= x < rows and 0 <= y < cols:
                s += all[x][y]

        sCount = 0
        mCount = 0
        for i in list(s):
            if i == "S":
                sCount += 1
            if i == "M":
                mCount += 1
        if len(s) == 4:
            first = f"{s[0]}A{s[1]}"
            second = f"{s[2]}A{s[3]}"
            if first in ("MAS", "SAM") and second in ("MAS", "SAM"):
                # print(s, sCount, mCount, f"{s[0]}A{s[1]}-{s[2]}A{s[3]}")
                return 1
        return 0

    for row in range((len(all))):
        for col in range(len(all[row])):
            if all[row][col] == "A":
                result += search(row, col)

    print(result)
