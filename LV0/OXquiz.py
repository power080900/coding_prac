# 'X[연산자]Y = Z' 형태의 quiz가 매개변수로 주어질 때 수식이 성립하면 O, 아니면 X를 return하는 함수를 작성하시오.
# 제한사항
# X, Y는 -10,000 이상 10,000 이하인 정수이다.
# Z는 -20,000 이상 20,000 이하인 정수이다.
# 연산자는 "+", "-"중 하나이다.

def solution(quiz):
    answer = []
    for i in quiz:
        i = i.replace(" = "," == ")
        if eval(i):
            answer.append("O")
        else:
            answer.append("X")
    return answer

print(solution(["1 + 2 = 3", "1 - 2 = -1", "1 - 2 = 1"])) # ['O', 'O', 'X']