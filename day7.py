# #pascals triangle
# numrow = 5
# triangle = []

# for i in range(numrow):
#     row = [1] * (i + 1)
#     for j in range(1, i):
#         row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#     triangle.append(row)
#     print(row)

# from typing import List

# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         # Sort the array
#         nums.sort()
        
#         # Two possible maximum products:
#         # 1. Product of the three largest numbers
#         # 2. Product of the two smallest (possibly negative) and the largest number
#         return max(nums[-1] * nums[-2] * nums[-3],
#                    nums[0] * nums[1] * nums[-1])

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         # Mapping of Roman numerals to integers
#         roman_map = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
        
#         total = 0
#         prev_value = 0
        
#         # Traverse the string from right to left
#         for char in reversed(s):
#             value = roman_map[char]
#             if value < prev_value:
#                 # Subtractive case (e.g., IV = 4, IX = 9)
#                 total -= value
#             else:
#                 total += value
#             prev_value = value
        
#         return total

