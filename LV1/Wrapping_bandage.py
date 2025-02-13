# 붕대감기 기술의 시전시간과 회복량, 추가회복량을 담은 1차원 정수 배열 bandage와 최대 체력 health, 몬스터의 공격시간과 피해량을 담은 2차원 배열 attack이 매개변수로 주어질 때,
# 모든 공격이 끝난 직후 남은 체력을 return하도록 함수를 작성하시오.
# 제한사항
# 공격을 받고 체력이 0이하가 되면 -1을 return한다.
# bandage는 [시전시간, 회복량, 추가회복량]을 담은 길이 3인 배열이다.
# 시전시간은 1 이상 50 이하의 자연수이다.
# 초당 회복량은 1 이상 100 이하의 자연수이다.
# 추가 회복량은 1 이상 100 이하의 자연수이다.
# health는 1 이상 1,000 이하의 자연수이다.
# attack의 길이는 1 이상 100 이하이다.
# attack[i]는 [공격시간, 피해량]을 담은 길이 2인 배열이다.
# 공격시간은 1 이상 1,000 이하의 자연수이다.
# 피해량은 1 이상 100 이하의 자연수이다.

def solution(bandage, health, attacks):
    heal_time = 0
    now = "heal"
    max_health = health
    game_time = attacks[-1][0] + 1
    answer = -1
    for sec in range(game_time):
        for attack in attacks:
            if attack[0] == sec:
                health -= attack[-1]
                heal_time = 0
                now = "attack"
        if health <= 0:
            answer = -1
            break
        if max_health > health and now != "attack":
            heal_time += 1
            health += bandage[1]
            if heal_time == bandage[0]:
                health += bandage[-1]
                heal_time = 0
            health = min(max_health, health)
            
        now = "heal"
        answer = health
    return answer

q1_bandage = [5, 1, 5]
q1_health = 30
q1_attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]

print(solution(q1_bandage, q1_health, q1_attacks)) # 5