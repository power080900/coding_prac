# 두 문자열 s, skip과 자연수 index가 주어질 때, 아래의 규칙을 반복하여 변환한 새로운 s를 반환한 결과를 return하도록 함수를 작성하시오.
# 제한사항
# s의 길이는 5 이상 50 이하이다.
# skip의 길이는 1 이상 10 이하이다.
# s와 skip은 알파벳 소문자로만 이루어져 있다.
# index는 1 이상 20 이하이다.

# 변환 규칙
# 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 변환한다.
# index만큼 뒤에 알파벳이 없는 경우에는 다시 a로 돌아간다.
# skip에 있는 알파벳은 제외하고 건너 뛴다.



def solution(s, skip, index):
    alphabet = [chr(i) for i in range(97, 123)]
    answer = ''
    for ss in skip:
        alphabet.remove(ss)
    
    for target in s:
        target_idx = alphabet.index(target)
        new_idx = (target_idx + index) % len(alphabet)
        new_lt = alphabet[new_idx]
        answer += new_lt
    
    return answer

q1_s = "aukks"
q1_skip = "wbqd"
q1_index = 5

print(solution(q1_s, q1_skip, q1_index)) # "happy"