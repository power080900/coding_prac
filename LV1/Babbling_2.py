# 문자열 배열 babbling이 매개변수로 주어질 때, 발음 할 수 있는 단어의 개수를 return 하도록 함수를 작성하시오.
# 제한사항
# babbling의 길이는 1 이상 100 이하이다.
# babbling의 원소는 길이가 1 이상 30 이하인 알파벳 소문자 문자열이다.
# 발음이 가능한 단어는 "aya","ye","woo","ma" 이다.
# 같은 발음을 연속해서 2번 이상 할 수 없다.

def solution(babbling):
    answer = 0
    cans = ["aya","ye","woo","ma"]
    cannots = ['ayaaya','yeye','woowoo','mama']
    new_babs = []
    for bab in babbling:
        for cannot in cannots:
            bab = bab.replace(cannot,'1')
        if not bab == "" and '1' not in bab:
            new_babs.append(bab)
    for new_bab in new_babs:
        for can in cans:
            new_bab = new_bab.replace(can,' ')
        
        if new_bab.strip() == "":
            answer += 1
               
    return answer

q1_babbling = ["aya", "yee", "u", "maa"]
q2_babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]

print(solution(q1_babbling)) # 1
print(solution(q2_babbling)) # 2
