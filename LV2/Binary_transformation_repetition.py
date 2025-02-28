# 0과 1로 이뤄진 문자열 s가 주어질 때 s가 1이 될 때까지 이진변환을 수행하고 그 과정에 제거된 모든 0의 개수를 각각 배열에 담아 return하는 함수를 작성하시오.
# 제한사항
# s의 길이는 1 이상 150,000 이하이다.
# s에는 1이 최소 하나 이상 포함되어 있다.
# s의 모든 0을 제거한다
# s의 길이를 c라고 하면 s를 "c를 2진법으로 표현한 문자열"로 바꾼다.

def solution(s):
    z = 0
    re = 0
    num = s
    while num != 1:
        z += str(num).count("0")
        num = int(str(num).replace("0",""))
        re += 1
        num = int(bin(len(str(num)))[2:])
    answer = [re, z]
    return answer

q1 = "110010101001"
q2 = "01110"
q3 = "1111111"

print(solution(q1)) # [3,8]
print(solution(q2)) # [3,3]
print(solution(q3)) # [4,1]
