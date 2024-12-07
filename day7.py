# # from collections import defaultdict
#
# with open("./sample/day7.txt", "r") as f:
#     result = 0
#     for line in f:
#         line = line.strip()
#
#         total, nums = line.split(":")
#         total = int(total.strip())
#         nums = list(map(int, nums.strip().split(" ")))
#
#         def backtrack(value, i):
#             if i == len(nums):
#                 if value == total:
#                     return True
#                 return False
#             if value > total:
#                 return False
#             return backtrack(value * nums[i], i + 1) or backtrack(
#                 value + nums[i], i + 1
#             )
#
#         if backtrack(nums[0], 1):
#             print(total, nums, "CORRECT")
#             result += total
#         print(total, nums)
#     print(result)
# PART 2
# from collections import defaultdict

with open("./sample/day7.txt", "r") as f:
    result = 0
    for line in f:
        line = line.strip()

        total, nums = line.split(":")
        total = int(total.strip())
        nums = list(map(int, nums.strip().split(" ")))

        def backtrack(value, i):
            if i == len(nums):
                if value == total:
                    return True
                return False
            if value > total:
                return False
            return (
                backtrack(value * nums[i], i + 1)
                or backtrack(value + nums[i], i + 1)
                or backtrack(int(f"{value}{nums[i]}"), i + 1)
            )

        if backtrack(nums[0], 1):
            print(total, nums, "CORRECT")
            result += total
        print(total, nums)
    print(result)
