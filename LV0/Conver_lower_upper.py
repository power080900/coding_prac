# 문자열 str이 주어질때 대문자는 소문자로, 소문자는 대문자로 변환하여 return하는 함수를 작성하시오.
# 제한사항
# str은 길이 1 이상 20 이하인 알파벳으로 이루어진 문자열이다.

def solution(str):
    return str.swapcase()

q1 = "HelloWorld"

print(solution(q1)) # hELLOwORLD