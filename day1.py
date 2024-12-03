# with open("./sample/day1.txt", "r") as f:
#     aa = []
#     bb = []
#     for line in f:
#         line = line.strip()
#         a, b = list(map(int, line.split()))
#         aa.append(a)
#         bb.append(b)
#     aa.sort()
#     bb.sort()
#     result = 0
#     for i in range(len(aa)):
#         result += abs(aa[i] - bb[i])
#     print(result)

# Part 2
from collections import defaultdict

with open("./sample/day1.txt", "r") as f:
    aa = []
    bb = []
    c = defaultdict(int)
    for line in f:
        line = line.strip()
        a, b = list(map(int, line.split()))
        aa.append(a)
        bb.append(b)
        c[b] += 1
    aa.sort()
    bb.sort()
    result = 0
    for i in range(len(aa)):
        result += aa[i] * c[aa[i]]
    print(result)
