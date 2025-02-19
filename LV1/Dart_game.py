# 0 ~ 10사이의 정수와 S,D,T,*,#로 이뤄진 문자열이 입력될 시 총 점수를 return하는 함수를 작성하시오.
# 제한사항
# 정수는 0 이상 10 이하이다.
# S는 1제곱, D는 2제곱, T는 3제곱을 의미한다.
# *은 해당 점수와 바로 직전 점수를 2배로 만든다.
# #은 해당 점수를 음수로 만든다.
# *은 첫 번째 기회에서 나올 수 있다.
# *과 #의 효과는 중첩될 수 있다.
# #가 중첩되는 경우 -2배가 된다.
# *이 중첩되는 경우 4배가 된다.

def solution(dartResult):
    num = []
    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            num[-1] = int(num[-1])
        elif dartResult[i] == 'D':
            num[-1] = int(num[-1]) ** 2
        elif dartResult[i] == 'T':
            num[-1] = int(num[-1]) ** 3
        elif dartResult[i] == '*':
            num[-1] = int(num[-1]) * 2
            try:
                num[-2] = int(num[-2]) * 2
            except:
                pass
        elif dartResult[i] == '#':
            num[-1] = int(num[-1]) * -1
        elif dartResult[i] == '0' and dartResult[i-1] == '1':
            num[-1] = 10
        else:
            num.append(int(dartResult[i]))
    return sum(num)

q1 = "1S2D*3T"
q2 = "1D2S#10S"
q3 = "1D2S0T"

print(solution(q1)) # 37
print(solution(q2)) # 9
print(solution(q3)) # 3