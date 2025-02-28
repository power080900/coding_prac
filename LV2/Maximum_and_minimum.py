# 공백으로 구분된 숫자들이 저장된 문자열 s가 주어질때 s가 나타내는 숫자들중 최솟값과 최댓값을 찾아 "(최솟값) (최댓값)" 형태의 문자열을 return하는 함수를 작성하시오.
# 제한사항
# s는 둘 이상의 정수가 공백으로 구분되어 있는 문자열이다.

def solution(s):
    s = s.split(" ")
    answer = []
    for i in s:
        answer.append(int(i))
    return f"{str(min(answer))} {str(max(answer))}"

q1 = "1 2 3 4"
q2 = "-4 -3 -2 -1"

print(solution(q1)) # "1 4"
print(solution(q2)) # "-4 -1"