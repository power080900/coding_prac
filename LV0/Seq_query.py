# 정수 배열 arr과 2차원 배열 queries가 매개변수로 주어지며, queries의 원소는 각각 하나의 query를 나타낸다. query의 모든 i 에 대해 k보다 크면서 가장 작은 arr[i]를 찾는 함수를 작성하시오.
# 제한사항
# query는 [s, e, k]의 형태이다.
# i 는 s 이상 e 이하이다.
# arr의 길이는 1 이상 1,000 이하이며 arr[i]는 0 이상 1,000,000 이하이다.
# queries의 길이는 1 이상 1,000 이하이다.
# k는 0 이상 1,000,000 이하이다.
# s는 0 이상 e 이하이다.
# e는 s 이상 arr의 길이 미만이다.
# query의 답이 존재하지 않으면 -1을 입력한다.

def solution(arr, queries):
    answer = []    
    for s, e, k in queries:
        temp = []
        for i in range(e, s-1, -1):
            if arr[i] > k:
                temp.append(arr[i])
        if temp == []:
            temp.append(-1)
        answer.append(min(temp))
    return answer

q1_arr = [0, 1, 2, 4, 3]
q1_queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

print(solution(q1_arr, q1_queries)) # [3, 4, -1]
