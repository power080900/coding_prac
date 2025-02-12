# 친구목록을 담은 1차원 배열 friends와 선물을 주고받은 기록을 담은 1차원 문자연 배열 gifts가 매개변수로 주어질 때, 다음 달에 가장 많은 선물을 받는 친구가 받은 선물의 수를 return하는 함수를 작성하시오.
# 제한사항
# friends의 길이는 2 이상 50 이하이다.
# friends[i]는 길이가 10 이하인 알파벳 소문자 문자열이다.
# friends에 중복된 이름은 없다.
# gifts의 길이는 1 이상 10,000 이하이다.
# gifts[i]는 "A B"형태의 문자열이며 A와 B가 같은 경우는 없다.
# A는 선물을 준 친구의 이름이며 B는 선물을 받은 친구의 이름이다.
# 선물을 주고 받은 기록이 있다면 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받는다.
# 선물을 주고 받은 기록이 없거나 주고 받은 수가 같다면 선물 지수가 더 큰 사람이 다음 달에 선물을 하나 받는다.
# 선물지수는 자신이 모든 친구들에게 선물을 준 수에서 받은 선물을 뺏 값이다.
# 만약 선물지수도 같다면 다음 달에 선물을 주고 받지 않는다.

def solution(friends, gifts):
    answer = 0
    df1 = {}
    df2 = {}
    
    for i in friends:
        df1[i] = {}
        df2[i] = 0
        for j in friends:
            if i != j:
                df1[i][j] = 0
    
    for gift in gifts:
        givers, receivers = gift.split()
        df1[givers][receivers] += 1
        df1[receivers][givers] -= 1
        df2[givers] += 1
        df2[receivers] -= 1
    
    
    for i in friends:
        temp = 0
        for receive, j in df1[i].items():
            if j > 0:
                temp += 1
            elif j == 0:
                if df2[i] > df2[receive]:
                    temp += 1
        answer = max(answer, temp)
    return answer

                
q1_friends = ["muzi", "ryan", "frodo", "neo"]
q1_gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
q2_friends = ["joy", "brad", "alessandro", "conan", "david"]
q2_gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

print(solution(q1_friends, q1_gifts)) # 2
print(solution(q2_friends, q2_gifts)) # 4

