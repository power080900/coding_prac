# 정수 l과 r이 주어졌을때 l이상 r이하의 정수중에서 0과 5로만 이루어진 모든 정수를 오름차순으로정리한 배열을 return하는 함수를 작성하시오.
# 제한사항
# l은 1 이상 r 이하이다.
# r은 l 이상 1,000,000 이하이다.
# 배열이 존재하지 않으면 [-1]을 return한다.

def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if set(str(i)) <= {'0', '5'}:
            answer.append(i)
    if answer == []:
        return [-1]
    else:
        return answer

print(solution(5, 555)) # [5, 50, 55, 500, 505, 550, 555]
print(solution(10, 20)) # -1
print(solution(7,5)) # -1
print(solution(6,554)) # [5, 50, 55, 500, 505, 550]
print(solution(1, 1000000))
