# 알파벳이 남긴 배열 spell과 사전 dic이 매개변수로 주어질때 spell에 담긴 알파벳을 1번씩만 모두 사용한 단어가 dic에 존재하면 1, 아니면 2를 return하는 함수를 작성하시오.
# 제한사항
# spell과 dic은 알파벳 소문자로만 이루어져 있다
# spell은 2 이상 10 이하이다.
# dic은 1 이상 10 이하이다.
# spell의 원소길이는 1이다.
# dic의 원소길이는 1이상 10이하이다.
# spell의 원소를 모두 사용해 만들 수 있는 단어는 dic에 단 하나만 존재한다.
# dic과 spell 모두 중복된 원소를 갖지 않는다.
# spell의 원소를 모두 사용해야 한다.

def solution(spell, dic):
    spell = set(spell)
    for i in dic:
        if spell.issubset(set(i)):
            return 1
    return 2

q1_spell = ['p','o','s']
q1_dic = ["sod", "eocd", "qixm", "adio", "soo"]
q2_spell = ["z", "d", "x"]
q2_dic = ["def", "dww", "dzx", "loveaw"]

print(solution(q1_spell, q1_dic)) # 2
print(solution(q2_spell, q2_dic)) # 1