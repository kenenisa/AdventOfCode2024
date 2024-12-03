# from collections import defaultdict

# with open("./sample/day2.txt", "r") as f:
#     safe = 0
#     for line in f:
#         line = line.strip()
#         a = list(map(int, line.split()))
#         diff = a[0] - a[1] > 0
#         valid = True
#         for i in range(len(a) - 1):
#             d = a[i] - a[i + 1]
#             currentDiff = d > 0
#             inRange = 1 <= abs(d) <= 3
#             if diff != currentDiff or not inRange:
#                 valid = False
#                 break
#         if valid:
#             safe += 1
#     print(safe)

# Part 2


def isValid(a):
    diff = a[0] - a[1] > 0
    valid = True
    for i in range(len(a) - 1):
        d = a[i] - a[i + 1]
        currentDiff = d > 0
        inRange = 1 <= abs(d) <= 3
        if diff != currentDiff or not inRange:
            valid = False
            break
    return valid


with open("./sample/day2.txt", "r") as f:
    safe = 0
    for line in f:
        line = line.strip()
        a = list(map(int, line.split()))
        if isValid(a):
            safe += 1
            continue
        valid = False
        for i in range(len(a)):
            newa = []
            for j in range(len(a)):
                if i != j:
                    newa.append(a[j])

            if isValid(newa):
                valid = True
                break
        if valid:
            print(a)
            safe += 1

    print(safe)
