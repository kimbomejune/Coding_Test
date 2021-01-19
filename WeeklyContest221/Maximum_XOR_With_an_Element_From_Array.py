# MaximumXORWithanElementFromArray

# You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].
# nums라는 정수형 데이터가 들어간 배열, queries라는 [xi, mi]형식의 데이터가 들어간 2차원 배열이 있다.
# The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi.
# i번째 쿼리의 대한 답은 xi의 최대 비트 XOR 값과 mi를 초과하지 않는 숫자요소
# In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.
# 즉, answer의 값은 max(nums[j] XOR xi)이며 nums[j]는 mi보다 같거나 작다. 만약 모든 nums의 모든 원소들이 mi보다 크다면 answer의 값은 -1
# Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.
# 반환값은 정수형 배열 answer이고 answer의 길이는 queries의 길이와 같으며 queries[i]의 대한 반환값은 answer[i]에 있다

"""
EX)
Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output: [3,3,7]
Explanation:
1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.
"""

"""
Constraints)
1 <= nums.length, queries.length <= 105
queries[i].length == 2
0 <= nums[j], xi, mi <= 109
"""

# ==========================================
#                 START !!!
# ==========================================

from typing import List


def MaximumXORWithanElementFromArray(nums: List, queries: List[List[int]]) -> List[int]:
    answer = [-1 for i in range(len(queries))]
    search_max = []
    for i in range(0, len(queries)):
        search_max.clear()
        for j in range(0, len(nums)):
            if(nums[j] <= queries[i][1]): search_max.append(int(bin(nums[j] ^ queries[i][0]), 2))
            else: search_max.append(-1)
        answer[i] = max(search_max)
    return answer


testA1 = [0,1,2,3,4]
testA2 = [[3,1],
          [1,3],
          [5,6]]
testB1 = [5,2,4,6,6,3]
testB2 = [[12,4],
          [8,1],
          [6,3]]

print(MaximumXORWithanElementFromArray(testB1, testB2))