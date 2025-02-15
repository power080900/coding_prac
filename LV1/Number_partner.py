# 두 정수 X,Y의 임의자리에서 공통으로 나타나는 정수(k)를 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라고 할 때, 두 수의 짝꿍을 return 하는 함수를 작성하시오.
# 제한사항
# X,Y의 자릿수는 3 이상 3,000,000 이하의 자연수이다.
# X,Y는 0으로 시작하지 않는다.
# k는 0 이상 9 이하의 정수이다.
# X,Y의 짝꿍이 없을 경우 -1, 0으로만 이루어진다면 0을 return 한다.

def solution(X, Y):
    answer = ""
    for i in range(9,-1,-1):
        a = X.count(str(i))
        b = Y.count(str(i))
        answer += str(i) * min(a,b)
    if answer == "":
        return "-1"
    elif answer[0] == "0":
        return "0"
    else:
        return answer
    
q1_X = "100"
q1_Y = "2345"
q2_X = "100"
q2_Y = "203045"
q3_X = "100"
q3_Y = "123450"
q4_X = "12321"
q4_Y = "42531"
q5_X = "5525"
q5_Y = "1255"

print(solution(q1_X, q1_Y)) # "-1"
print(solution(q2_X, q2_Y)) # "0"
print(solution(q3_X, q3_Y)) # "10"
print(solution(q4_X, q4_Y)) # "321"
print(solution(q5_X, q5_Y)) # "552"