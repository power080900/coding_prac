# 전체 스테이지를 N, 현재 게임을 진행하고 있는 사용자가 멈춘 스테이지 번호가 담긴 배열 stages가 매개변수로 주어질 때,
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 함수 작성하시오.
# 제한사항
# 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
# stages의 길이는 1 이상 200,000 이하이다.
# stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
# 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
# 실패율은 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수로 정의한다.
# 스테이지에 도달한 플레이어가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
# 실패율이 같은 스테이지의 번호는 작은 번호가 먼저 오도록 하면 된다.

def solution(N, stages):
    answer = []
    rate = {}
    for i in range(1,N+1):
        j = [j for j in stages if j >= i]
        if len(j) != 0:
            rate[i] = stages.count(i)/len(j)
        else :
            rate[i] = 0
    answer = sorted(rate.items(),key=lambda x: x[1], reverse=True)
    return list(zip(*answer))[0]

q1_N = 5
q1_stages = [2, 1, 2, 6, 2, 4, 3, 3]
q2_N = 4
q2_stages = [4,4,4,4,4]

print(solution(q1_N, q1_stages)) # [3,4,2,1,5]
print(solution(q2_N, q2_stages)) # [4,1,2,3]