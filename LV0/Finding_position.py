# 방향키 keyinput과 맵의 크기 board가 매개변수로 주어질때 keyinput에 따라 이동한 후의 캐릭터 좌표 [x, y]를 return하는 함수를 작성하시오.
# 제한사항
# board는 [가로, 세로]의 형태로 주어진다.
# board의 가로와 세로틑 홀수이다.
# board 밖으로 벗어난 방향키 임력은 무시한다.
# keyinput의길이는 0 이상 50 이하이다.
# board의 크기는 1 이상 99 이하이다.
# keyinput은 "up", "down", "left", "right"로만 주어진다.

def solution(keyinput, board):
    answer = [0, 0]
    for i in keyinput:
        if i == "up" and answer[1] < int(board[1]/2):
            answer[1] += 1
        elif i == "down" and answer[1] > -int(board[1]/2):
            answer[1] -= 1
        elif i == "left" and answer[0] > -int(board[0]/2):
            answer[0] -= 1
        elif i == "right" and answer[0] < int(board[0]/2):
            answer[0] += 1
    return answer

q1_key = ["left", "right", "up", "right", "right"]
q1_board = [11,11]
q2_key = ["down", "down", "down", "down", "down"]
q2_board = [7,9]

print(solution(q1_key, q1_board)) # [2, 1]
print(solution(q2_key, q2_board)) # [0, -4]