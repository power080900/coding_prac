# 2차원 board 배열에 지뢰가 있는 곳은 1로 없는 지역은 0으로 표시되어 있다. 지뢰의 주변 8방향은 모두 위험지역으로 분류할 때 안전한 지역의 칸수를 return하는 함수를 작성하시오.
# 제한사항
# board는 N * N 크기의 2차원 배열이다.
# N은 1 이상 100 이하의 자연수이다.
# board의 원소는 0 또는 1이다.

def solution(board):
    n = len(board)
    answer = n * n
    danger_zone = set() 
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),  (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                danger_zone.add((i, j))
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        danger_zone.add((ni, nj))
    
    return answer - len(danger_zone)
                
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])) # 16