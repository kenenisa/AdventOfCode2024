#
# # from collections import defaultdict
# with open("./sample/day9.txt", "r") as f:
#     result = 0
#     line = ""
#     for ln in f:
#         line = ln.strip()
#     id = 0
#     blocks = []
#
#     for i in range(0, len(line), 2):
#         blocks += [id] * int(line[i])
#         if i + 1 < len(line):
#             blocks += ["."] * int(line[i + 1])
#         id += 1
#     n = len(blocks)
#     right = n - 1
#     for i in range(n):
#         if blocks[i] != ".":
#             continue
#         while right > i and blocks[right] == ".":
#             right -= 1
#         blocks[i], blocks[right] = blocks[right], blocks[i]
#     for i in range(n):
#         if blocks[i] == ".":
#             break
#         result += i * blocks[i]
#
#     print(blocks)
#     print("".join(map(str, blocks)))
#
#     print(result)
# from collections import defaultdict
#
# Part 2

with open("./sample/day9.txt", "r") as f:
    result = 0
    line = ""
    for ln in f:
        line = ln.strip()
    id = 0
    blocks = []

    freeSpace = []
    fileSpace = []
    for i in range(0, len(line), 2):
        fileSpace.append((id, int(line[i]), len(blocks)))
        blocks += [id] * int(line[i])
        if i + 1 < len(line):
            freeSpace.append((len(blocks), int(line[i + 1])))
            blocks += ["."] * int(line[i + 1])
        id += 1
    print("".join(map(str, blocks)))
    n = len(blocks)
    right = n - 1

    for i in range(len(fileSpace) - 1, -1, -1):
        ID, amount, delPos = fileSpace[i]
        for k in range(i + 1):
            pos, length = freeSpace[k]
            if amount <= length:
                for j in range(amount):
                    blocks[pos + j] = ID
                    blocks[delPos + j] = "."
                freeSpace[k] = (pos + amount, length - amount)
                break
    for i in range(n):
        if blocks[i] == ".":
            continue
        result += i * blocks[i]

    print("".join(map(str, blocks)))

    print(result)
