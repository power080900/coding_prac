# "(" 또는 ")"로만 이뤄진 문자열 s가 주어졌을 때,
# s가 유효한 괄호이면 true를 반환하고, 그렇지 않으면 false를 return하는 함수를 작성하시오.
# 제한사항
# 문자열 s의 길이는 100,000 이하인 자연수이다.
# 문자열 s는 "(" 또는 ")"로만 이루어져 있다.

def solution(s):
    answer = False
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == "(" and i == ")":
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        answer = True
    return answer

q1 = "()()"
q2 = "(())()"
q3 = ")()("
q4 = "(()("

print(solution(q1)) # True
print(solution(q2)) # True
print(solution(q3)) # False
print(solution(q4)) # False

