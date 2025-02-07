# 아기는 'aya', 'ye', 'woo','ma'를 최대 한번씩 사용해 조합한 발음만 한다.
# 문자열 babbling이 매개변수로 주어질 때 조카가발음 할 수 있는 단어의 개수를 return 하도록 solution 함수를 작성하라.
# 제한사항
# babbling의 길이는 1 이상 100 이하이다.
# babbling[i]의 길이는 1 이상 15 이하이다.
# babbling의 각 문자열에서 'aya', 'ye', 'woo', 'ma'는 최대 한번씩만 사용한다.
# babbling의 각 문자열은 소문자로만 이루어져 있다.

def solution(babbling):
    answer = 0
    for i in babbling:
        i = i.replace('aya', ' ').replace('ye', ' ').replace('woo', ' ').replace('ma', ' ')
        i = i.lstrip().rstrip()
        if i == '':
            answer += 1
    return answer

print(solution(["aya", "yee", 'u', 'maa','wyeoo'])) # 1