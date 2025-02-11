# 정수배열 arr가 매개변수로 주어질 때 무작위로 뽑은 숫자가 arr의 순서대로 뽑힐 것이라고 가정한다. 이때 완성된 배열을 return하는 함수를 작성하시오.
# 제한사항
# 완성된 배열의 길이가 k보다 작으면 -1을 나머지 값에 추가하여 return한다.
# arr의 길이는 1 이상 100,000 이하이다.
# arr[i]의길이는 0 이상 100,000 이하이다.
# k는 1 이상 1,000 이하이다.

def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    answer = answer[:k]
    len_a = len(answer)
    if len_a <= k:
        for i in range(k-len_a):
            answer.append(-1)
    return answer

q1_arr = [0,1,1,1,1]
q1_k = 4

print(solution(q1_arr, q1_k)) # [0, 1, -1, -1]
