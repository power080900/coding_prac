# 이차원 정수 배열 arr가 매개변수로 주어질때 열과 행이 같아지도록 부족한 부분을 0으로 채운 이차원 배열을 return하는 함수를 작성하시오.
# 제한사항
# arr의 길이는 1 이상 100 이하이다.
# arr[i]는 1 이상 100 이하이다.
# arr[i]의 원소는 1 이상 1,000 이하이다.

def solution(arr):
    answer = []
    n = len(arr)
    m = len(arr[0])
    if n == m:
        return arr
    elif n < m:
        for i in range(n):
            answer.append(arr[i])
        for j in range(m - n):
            answer.append([0] * m)
    else:
        for i in range(n):
            for j in range(n-m):
                arr[i].append(0)
            answer.append(arr[i])

    return answer

q1_arr = [[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]
q2_arr = [[57, 192, 534, 2], [9, 345, 192, 999]]

print(solution(q1_arr)) # [[572, 22, 37, 0], [287, 726, 384, 0], [85, 137, 292, 0], [487, 13, 876, 0]]
print(solution(q2_arr)) # [[57, 192, 534, 2], [9, 345, 192, 999], [0, 0, 0, 0], [0, 0, 0, 0]]