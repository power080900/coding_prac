# 지갑의 가로와 세로의 크기를 담은 정수리스트 wallet과 지페의 가로와 세로의 크기를 담은 정수리스트 bill이 주어질 때, 
# 지갑의 크기가 지폐의 크기보다 크거나 같아질 때까지 지갑의 크기를 반으로 줄이는 행동을 몇 번 해야 하는지 return 하도록 함수를 작성하시오.
# 제한사항
# wallet와 bill의 길이는 2이다.
# wallet[0]와 wallet[1]은 10 이상 100 이하의 자연수이다.
# bill[0]와 bill[1]은 10 이상 2,000 이하의 자연수이다.
# 지폐를 접을때는항상 길이가 긴쪽을 반으로 접는다.
# 접기 전 길이가 홀수라면 접은 후 소수점 이하는 버린다.
# 접힌 집히가 그대로 혹은 90도 돌려서 지갑에 들어가면 그만접는다.

def solution(wallet, bill):
    answer = 0
    while not (min(wallet) >= min(bill) and max(wallet) >= max(bill)):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
    return answer

q1_wallet = [30, 15]
q1_bill = [26, 17]
q2_wallet = [50, 50]
q2_bill = [100, 241]

print(solution(q1_wallet, q1_bill)) # 1
print(solution(q2_wallet, q2_bill)) # 4