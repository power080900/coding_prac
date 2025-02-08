# 등차 혹은 등비 수열 common이 매개변수로 주어질때 마지막 원소 다음으로올 숫자를 return하는 함수를 작성하시오.
# 제한사항
# common의 길이는 2 이상 1,000 이하이다.
# common[i]는 -1,000 이상 2,000 이하인 정수이다.
# 등비수열의 공비는 0이 아닌 정수이다.

def solution(common):
    a1 = common[-1] - common[-2]
    a2 = common[-2] - common[-3]
    if a1 == a2:
        return common[-1] + a1
    else:
        return common[-1] ** 2 / common[-2]
    
print(solution([1, 2, 3, 4])) # 5
print(solution([2,4,8,16])) # 32