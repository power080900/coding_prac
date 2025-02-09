# 문자열 code를 읽으면서 문자가 "1"이 나오면 mode를 바꾸며, mode에 따라 code를 읽어가며 문자열 ret을 만든다.
# 제한사항
# mode는 0 또는 1이다.
# idx를 0부터 시작하여 code의 길이 -1까지 증가시키며 code[idx]의 값에 따라 행동한다.
# mode가 0일 때 code[idx]가 "1"이면 mode를 0에서 1로 바꾸며, "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가한다.
# mode가 1일 때 code[idx]가 "1"이면 mode를 1에서 0으로 바꾸며, "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가한다.
# code의 길이는 1 이상 100,000 이하이며, 알파벳 소문자 또는 "1"로만 이루어져 있다.
# 단, return하려는 ret이 빈문자열이면 "EMPTY"를 반환한다.

def solution(code):
    mode = 0
    ret = ""
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == "1":
                mode = 1
            elif idx % 2 == 0:
                ret += code[idx]
        else:
            if code[idx] == "1":
                mode = 0
            elif idx % 2 == 1:
                ret += code[idx]
    if ret == "":
        return "EMPTY"
    return ret

print(solution("abc1abc1abc")) # "acbac"