# 문자열 s가 주어졌을 때 JadenCase로 바꾼 문자열을 return하는 함수를 작성하시오.
# 제한사항
# JadenCase란 모든 단어의 첫 문자가 대문자이고 그 외의 알파벳은 소문자인 문자열이다.
# 문자열 s는 길이 1 이상 200 이하인 문자열이다.
# s는 알파벳과 숫자, 공백문자(" ")로 이루어져있다.
# 숫자는 단어의첫 문자로만 나온다
# 숫자로만 이뤄진 단어는 없다
# 공백이 연속으로 나올 수 있다.

def solution(s):
    answer = []
    s = s.split(" ")
    for i in range(len(s)):
        if len(s[i]) > 1:
            answer.append(s[i][0].upper() + s[i][1:].lower())
        else:
            # print(s[i])
            answer.append(s[i].upper())
    return " ".join(answer)

q1 = "3people unFollowed me"
q2 = "for the last week"

print(solution(q1)) # "3people Unfollowed Me"
print(solution(q2)) # "For The Last Week"