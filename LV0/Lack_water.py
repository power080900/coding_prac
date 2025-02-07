# 저수지에 저장된 물의 양을 나타내는 storage와 지난달 사용량을 나타내는 usage, 변화량을 나타내는 리스트 change가 주어질때 몇 달 후 물이 부족해지는 지 return 하도록 solution 함수를 완성하세요.
# 제한사항
# 기간이 끝난뒤 물이 남아있다면 -1을 return합니다.
# storage는 1,000 이상 1,000,000 이하의 자연수입니다.
# usage는 500 이상 30,000 이하의 자연수입니다.
# change의 길이는 1 이상 30 이하입니다.
# change[i]는 -99 이상 500 이하의 정수입니다.
# 매달 물 사용량은 소수점 이하를 버린 정수로 계산합니다

def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage += (usage * change[i]) // 100
        total_usage += usage
        if total_usage > storage:
            return i
    return -1

print(solution(1000, 2000, [-10, 25, -33])) # 0
print(solution(5141, 500, [10, -10, 10, -10, 10, -10, 10, -10, 10, -10])) # -1