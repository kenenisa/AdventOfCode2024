# import re
#
#
# with open("./sample/day3.txt", "r") as f:
#     aa = []
#     bb = []
#     all = ""
#     for line in f:
#         all += line
#     print(all)
#     pattern = r"mul\(\d{1,3},\d{1,3}\)"
#
#     matches = re.findall(pattern, all)
#     print(matches)
#     s = 0
#
#     for mul in matches:
#         first = int(mul.split("mul(")[1].split(",")[0])
#         second = int(mul.split(",")[1].split(")")[0])
#         s += first * second
#     print(s)
#
# Part 2
import re


with open("./sample/day3.txt", "r") as f:
    aa = []
    bb = []
    all = ""
    for line in f:
        all += line
    print(all)

    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"

    matches = re.findall(pattern, all)
    print(matches)
    s = 0

    active = True
    for mul in matches:
        if "mul" in mul and active:
            first = int(mul.split("mul(")[1].split(",")[0])
            second = int(mul.split(",")[1].split(")")[0])
            s += first * second
        else:
            active = mul == "do()"

    print(s)
