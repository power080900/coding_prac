# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 return 하는 함수를 작성하시오.
# 제한사항
# n은 2이상 1,000,000이하의 자연수이다.

def solution(n):
    a = [False,False] + [True]*(n-1)
    primes=[]
    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return len(primes)

q1_n = 10
q2_n = 5

print(solution(q1_n)) # 4
print(solution(q2_n)) # 3
