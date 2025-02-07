# 양의 정수 n이 매개변수로 주어지고 n x n 배열에1부터 n**2까지 정수를 [0][0]에서 시계방향으로 배치한 이차원 배열을 return하는 함수를 작성하라.
# 제한 사항
# n은 1 이상 30 이하인 양의 정수이다.

def solution(n):
    answer = [[0]*n for _ in range(n)]
    x, y = 0, 0
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    dir_idx = 0
    num = 1
    for _ in range(n*n):
        answer[x][y] = num
        num += 1
        nx, ny = x + dx[dir_idx], y + dy[dir_idx]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            dir_idx = (dir_idx + 1) % 4
            nx, ny = x + dx[dir_idx], y + dy[dir_idx]
        x, y = nx, ny
        print(answer)
    return answer

print(solution(3)) # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]