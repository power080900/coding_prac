# 문자열 my_string과 2차원 정수배열 queries개 매개변수로 주어질 때, my_string을 queries의 순서대로 처리한 후 return하는 함수를 작성하시오
# 제한사항
# my_string의 길이는 1 이상 1,000 이하의 영소문자로 이루어져있다.
# queries의 원소는 [s,e]의 형태이며 인덱스 s부터 e까지의 문자열을 뒤집으라는 의미이다.
# s는 0 이상 e 이하이다.
# e는 s 이상 my_string의 길이 이하이다.
# queries의 길이는 1 이상 1,000 이하이다.

def solution(my_string, queries):
    for s,e in queries:
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string

q1_my_string = "rermgorpsam"
q1_queries = [[2, 3], [0, 7], [5, 9], [6, 10]]

print(solution(q1_my_string, q1_queries)) # programmers