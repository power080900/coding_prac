# 문자열 s가 입력되었을때 일련의 과정을 거쳐 문자열을 분해하고 분해한 문자열의 개수를 return하는 함수를 작성하시오.
# 제한사항
# s의 길이는 1 이상 10,000 이하이다.
# s는 알파벳 소문자로만 이루어져 있다.
# 문자열을 읽어나가면서 읽은 첫 글자는 X라고 할때, X이후로 나온 문자들의 횟수를 각각 센다.
# 처음으로 두 횟수가 같아지는 순간 멈추고 그때까지의 문자열을 분리한다.
# 분리한 문자열을 뺴고 남은 부분에 대해서 같은 과정을 반복한다.
# 위의 과정을 반복하여 분리한 문자열의 개수를 return한다.

def solution(s):
    answer = 0
    first = 0
    others = 0
    last = ""
    for i in s:
        if i == last :
            first += 1
        elif first == 0:
            first += 1
            last = i
        elif i != last:
            others += 1
        if first == others:
            first = 0
            others = 0
            answer += 1
    if first != 0:
        answer += 1
    return answer

q1_s = "banana"
q2_s = "abracadabra"
q3_s = "aaabbaccccabba"

print(solution(q1_s)) # 3
print(solution(q2_s)) # 6
print(solution(q3_s)) # 3
