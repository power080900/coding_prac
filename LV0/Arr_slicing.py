# 정수 배열 arr와 query가 주어진다.
# 짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 뒷부분을 잘라서 버린다.
# 홀수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 앞부분을 잘라서 버린다.
# 작업후 남은 arr의 부분배열을 return하는 함수를 작성하시오.
# 제한사항
# arr의 길이는 5 이상 100,000 이하이다.
# arr[i]는 0 이상 100 이하이다.
# query의 길이는 1 이상 min(50, arr의 길이 /2) 이하이다.
# query[i]는 0 이상 남은 arr의 길이 미만이다.

def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr

print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2])) # [1, 2, 3]