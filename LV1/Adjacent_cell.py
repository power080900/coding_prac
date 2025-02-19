# 각 칸에 칠해진 색 이름이 담김 문자열 리스트 borad, 위치를 나타내는 정수 w, h가 주어질 때,
# board[h][w]와 인접한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return하도록 함수를 작성하시오.
# 제한사항
# board의 길이는 1 이상 7 이하이다.
# board의 길이와 board[i]의 길이는 동일하다.
# h,w는 0 이상 board의 길이 이하이다.
# board[h][w]의 길이는 1 이상 10 이하이며, 영어 소문자로 이뤄져있다.

def solution(board, h, w):
    answer = 0
    t_color = board[h][w]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dh, dw in directions:
        nh, nw = h+dh, w+dw
        if 0 <= nh < len(board) and 0 <= nw < len(board[0]) and board[nh][nw] == t_color:
            answer += 1
    
    return answer

q1_board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
q1_h = 1
q1_w = 1

print(solution(q1_board, q1_h, q1_w)) # 2