# 문자열 A와 B개 매개변수로 주어질 때 A의 문자열을 오른쪽으로 한자리씩 밀어서 B가 될 수 있다면 최소 횟수를 return하는 함수를 작성하시오
# 제한사항
# B가 될 수 없으면 -1을 return한다.
# A와 B의 길이는 1 이상 100 미만이다.
# A와 B는 알파벳 소문자로만 이루어져 있다.

def solution(A,B):
    n = A * 2
    B_idx = []
    if B in n:
        for i in range(len(n)):
            if n[i:len(B)+i] == B[0:len(B)+i]:
                B_idx.append(i)
        return len(B) - B_idx[-1]
    return -1
        

print(solution("hello", "ohell")) # 1
print(solution("apple", "elppa")) # -1
print(solution("atat", "tata")) # 1
print(solution("abc", "abc")) # 0

# hellohello
# atatatat