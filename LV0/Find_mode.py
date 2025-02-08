# 정수 배열 array가 매개변수로 주어질때 최빈값을 return하는 함수를 작성하시오.
# 제한사항
# 최빈값이 여러 개일 경우 -1을 return하시오.
# array의 길이는 0 초과 100 미만이다.
# array[i]는 0 이상 1000 이하이다.

def solution(array):
    answer = 0
    cnt = 0
    for i in set(array):
        if array.count(i) > cnt:
            cnt = array.count(i)
            answer = i
        elif array.count(i) == cnt:
            answer = -1
    return answer

print(solution([1,2,3,3,3,4])) # 3
print(solution([1,1,2,2])) # -1