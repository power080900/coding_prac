# 삼각형 두변의 길이가 담긴 배열 sides가 매개변수로 주어질 때 나머지 한 변이 될 수 있는 정수 개수를 return 하도록 solution 함수를 작성하시오.
# 제한사항
# sides[i]는 자연수이다.
# sides의 길이는 2이다.
# sides[0]는 1 이상 1000 이하인 자연수이다.

def solution(sides):
    a = max(sides)
    c = min(sides)
    answer = 0
    for i in range(1, a+c+1):
        if i > a - c and a + c > i:
            answer +=1
    return answer

q1_sides = [1, 2]
q2_sides = [3, 6]

print(solution(q1_sides)) # 1
print(solution(q2_sides)) # 5