# MaximumNumberOfEatenApples

# There is a special kind of apple tree that grows apples every day for n days.
# 매일 n개의 사과가 자라는 특별한 사과나무가 있다
# On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten.
# i번째 날에 사과는 applesList의 i번째 만큼 자라며 daysList의 i번째 날까지 먹을수있다. 현재 i + daysList의 i번째 값이 지나면 i번째 날에 열린 사과는 먹지 못한다.
# On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.
# 어느날에는 사과가 없는 날이 있다. 그때는 applesList의 i번째와 daysList의 i번째는 0이다.
# You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.
# 하루에 하나씩 사과를 먹기로하였다. 처음 n일 후에도 계속 먹을 수 있다는 것을 유의
# Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.
# n의 길이를 가진 두개의 정수형 배열 days와 apples, 반환값은 최대 먹을수 있는 사과의 수

"""
EX)
Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
Output: 7
Explanation: You can eat 7 apples:
- On the first day, you eat an apple that grew on the first day.
- On the second day, you eat an apple that grew on the second day.
- On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
- On the fourth to the seventh days, you eat apples that grew on the fourth day.
"""

"""
Constraints)
apples.length == n
days.length == n
1 <= n <= 2 * 10^4
0 <= apples[i], days[i] <= 2 * 10^4
days[i] = 0 if and only if apples[i] = 0.
"""

# ==========================================
#                 START !!!
# ==========================================

from typing import List
from heapq import heappop, heappush


def MaximumNumberOfEatenApples(apples: List[int], days: List[int]) -> int:
    heap = []
    res = 0
    n = len(apples)
    
    for i in range(n + max(days)):
        if i < n and apples[i] > 0 :
            heappush(heap, [i + days[i], apples[i]])
        if heap:
            heap[0][1] -= 1
            res+=1
        while heap and (heap[0][0] <= i + 1 or heap[0][1] == 0):
            heappop(heap)
    
    return res


print(MaximumNumberOfEatenApples([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]))