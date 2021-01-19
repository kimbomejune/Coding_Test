# WhereWilltheBallFall

# You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.
# m x n 사이즈의 2차원 그리드 박스와 공이있다. 그 박스는 위아래가 뚫려있는 형태이다.
# Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.
# 각 셀(m, n)에는 오른쪽 혹은 왼쪽으로 진행되는 선이 두개의 꼭짓점을 이루고있다.
# - A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
# 좌측 상단에서 우측 하단으로 이어지는 선은 그리드상으로 1로 표기한다
# - A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
# 우측 상단에서 좌측 하단으로 이어지는 선은 그리드상으로 -1로 표기한다.
# We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom.
# 각 column에 하나의 공을 넣는다. 이 공은 중간에 걸릴수도 있고 바닥으로 나갈수도 있다.
# A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.
# 중간에 걸리는 경우는 두개의 대각선이 V자 형태로 이루어졌을때 혹은 하나의 대각선 끝점이 박스의 벽과 이어져있을때 나타난다.
# Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after 
# dropping the ball from the [ith] column at the top, or -1 if the ball gets stuck in the box.
# 반환값은 n의 크기를 가진 answer이라는 배열이며 answer의 배열값은 각 column에서 공이 바닥까지 도달할수 있는가 없는가를 나타낸다.
# 공이 바닥에 도달한다면 answer[i]는 해당 공이 시작한 column 값을 가진다.
# 만약 i번째 column에서 아무것도 나오지 않는다면 answer[i] = -1

"""
EX)
Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.
"""

"""
Constraints)
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is 1 or -1.
"""

# ==========================================
#                 START !!!
# ==========================================

from typing import List


def WhereWilltheBallFall(grid: List[List[int]]) -> List[int]:
    row_size = len(grid)
    column_size = len(grid[0])   
    answer = [-1 for i in range(column_size)]  
    for column in range(0, column_size):
        column_position = column
        for row in range(0, row_size):
            row_position = row
            now_cell = grid[row_position][column_position]
            try:
                left_cell = grid[row_position][column_position - 1]
                right_cell = grid[row_position][column_position + 1]
            except:
                if column_position == 0:
                    if(now_cell == -1):
                        column_position = -1
                        break
                    else: right_cell = grid[row_position][column_position + 1]
                elif column_position == column_size - 1:
                    if(now_cell == 1):
                        column_position = -1
                        break
                    else: left_cell = grid[row_position][column_position - 1]
            if now_cell == left_cell != 1:
                column_position = column_position - 1
            elif now_cell == right_cell != -1:
                column_position = column_position + 1
            else:
                break
        if row_position == row_size - 1:
            answer[column] = column_position
            
    return answer


testA = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
testB = [[-1]]
testC = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
print(WhereWilltheBallFall(testB))