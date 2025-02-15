# 재료의 정보를 나타내는 ingredient가 매개변수로 주어질 때, 포장하는 햄버거의 개수를 return하는 함수를 작성하시오.
# 제한사항
# ingredient는 길이가 1 이상 1,000,000 이하인 정수배열이다.
# ingredient의 원소는 1,2,3 중 하나이며, 각각 순서대로 빵, 야채, 고기를 의미한다.
# 순서가 빵-야채-고기-빵인 경우에만 포장한다.

def solution(ingredient):
    answer = 0
    burger = []
    for i in ingredient:
        burger.append(i)
        if burger[-4:] == [1, 2, 3, 1]:
            answer += 1
            burger.pop()
            burger.pop()
            burger.pop()
            burger.pop()
    return answer

q1_ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
q2_ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]

print(solution(q1_ingredient)) # 2
print(solution(q2_ingredient)) # 0

