# 현재 인형뽑기 게임의 상태를 나타내는 board와 크레인을 작동시킨 위치가 담긴 moves가 매개변수로 주어질 때,
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 함수를 작성하시오.
# 제한사항
# board 배열은 5 x 5 이상 30 x 30 이하인 배열이다.
# board의 각 칸에는 0 이상 100 이하인 정수가 담겨있다.
# 0은 빈 칸을 나타낸다.
# 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타낸다.
# moves 배열의 크기는 1 이상 1,000 이하이다.
# moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수이다.
# 같은 모양의 인형 두개가 연속해서 쌓아면 인형은 터뜨려지면서 사라진다.

def solution(board, moves):
    bucket = []
    answer = 0
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                target = board[i][move-1]
                board[i][move-1] = 0

                if bucket and bucket[-1] == target:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(target)
                break
                
    return answer

q1_board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
q1_moves = [1,5,3,5,1,2,1,4]

print(solution(q1_board, q1_moves)) # 4