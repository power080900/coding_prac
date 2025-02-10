# 문자열 my_string, overwrite_string과 정수 s가 매개변수로 주어질 때 my_string의 인덱스 s부터 overwrite_string의 길이만큼 덮어쓴 문자열을 return하는 함수를 작성하시오.
# 제한사항
# my_string과 overwrite_string은 숫자와 알파벳으로 이루어져있다.
# overwrite_string의 길이는 1 이상 my_string의 길이 이하이다.
# my_string의 길이는 overwrite_string의 길이 이상 1,000 이하이다.
# s는 0 이상 my_string-overwrite_string의 길이 이하이다.

def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]

q1_my_string = "He11oWor1d"
q1_overwrite_string = "lloWorl"
q1_s = 2

print(solution(q1_my_string, q1_overwrite_string, q1_s)) # "HelloWorld"