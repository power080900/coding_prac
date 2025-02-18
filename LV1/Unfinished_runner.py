# 마라톤 참여자의 배열 paricipant와 완주한 선수들의 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return하는 함수를 작성하시오.
# 제한사항
# 참여한 선수의 수는 1명 이상 100,000명 이하이다.
# completion의 길이는 participant의 길이보다 1 작다.
# 참가자중 동명이인이 있을 수 있다.

import collections

def solution(p, c):   
    i = collections.Counter(p) - collections.Counter(c)
    return list(i.keys())[0]

q1_participant = ["leo", "kiki", "eden"]
q1_completion = ["eden", "kiki"]
q2_participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
q2_completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(q1_participant, q1_completion)) # "leo"
print(solution(q2_participant, q2_completion)) # "vinko"
