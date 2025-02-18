# 1번 키부터 차례대로 할당된 문자들이 순서대로담긴 문자열 배열을 keymap, 입력할 문자열들이 담긴 배열 target이 주어질 때,
# 각 문자열을 작성하기 위해 최소한 눌러야 하는 횟수를 순서대로 담아 return하는 함수를 작성하시오.
# 제한사항
# keymap의 길이는 1 이상 100 이하이다.
# keymap의 원소의 길이는 1 이상 100 이하이다.
# keymap[i]는 i+1번 키를 눌렀을대 순서대로 바뀌는 문자열을 의미한다
# keymap의 원소의 길이는 서로 다를 수 있으며, 알파벳 대문자로만 이뤄져있다.
# target의 길이는 1 이상 100 이하이다.
# target의 원소의 길이는 1 이상 100 이하이다.
# target의 원소는 알파벳 대문자로만 이뤄져있다.
# 단, 목표 문자열을 작성할 수 없을 경우 -1을 return한다.

def solution(keymap, targets):
    answer = []
    keymap_dict = {}

    for idx, key in enumerate(keymap):
        for press_cnt, char in enumerate(key):
            if char not in keymap_dict:
                keymap_dict[char] = press_cnt+1
            else:
                keymap_dict[char] = min(keymap_dict[char], press_cnt+1)

    for target in targets:
        press_cnt = 0
        for char in target:
            if char in keymap_dict:
                press_cnt += keymap_dict[char]
            else:
                press_cnt = -1
                break

        answer.append(press_cnt)

    return answer

q1_keymap = ["ABACD", "BCEFD"]
q1_targets = ["ABCD","AABB"]

q2_keymap = ["AA"]
q2_targets = ["B"]

q3_keymap = ["AGZ", "BSSS"]
q3_targets = ["ASA","BGZ"]

print(solution(q1_keymap, q1_targets)) # [9, 4]
print(solution(q2_keymap, q2_targets)) # [-1]
print(solution(q3_keymap, q3_targets)) # [4, 6]