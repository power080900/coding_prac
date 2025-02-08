# 연속된 수 num개를 더한 값이 total이 될때 정수를 오름차순으로 담아 return하는 함수를 작성하시오.
# 제한사항
# num은 1 이상 100 이하의 자연수이다.
# total은 0 이상 1000 이하의 정수이다.
# num개의 연속된 수를 더하여 total이 될 수 없는 케이스는 없다.

def solution(num, total):
    a = int(total / num - (num - 1) / 2)
    return [i for i in range(a, a + num)]

print(solution(3, 12)) # [3, 4, 5]
print(solution(5, 15)) # [1, 2, 3, 4, 5]