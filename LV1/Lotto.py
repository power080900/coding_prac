# 구매한 로또 번호를 담은배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어질 때,
# 당첨 가능한 최고 순위와 최저 순위를 배열에 담아 return 하도록 함수를 작성하시오.
# 제한사항
# lottos는 길이 6인 정수 배열이다.
# lottos의 모든 원소는 0 이상 45 이하인 정수이다.
# 0은 알아볼 수 없는 숫자를 의미한다.
# 0을 제외한 다른 숫자들은 lottos에 2개 이상 담겨있다.
# lottos의 원소들은 정렬되어 있지 않을 수 있다.
# win_nums은 길이 6인 정수 배열이다.
# win_nums의 모든 원소는 1 이상 45 이하인 정수이다.
# win_nums에는 같은 숫자가 2개 이상 담겨있지 않다.
# win_nums의 원소들은 정렬되어 있지 않을 수 있다.

def solution(lottos, win_nums):
    match = 0
    answer = []
    un = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            match += 1
    if un == 0 and match ==0:
        answer = [6,6]
    elif match == 0:
        answer = [7-(match+un),6-match]
    else:
        answer = [7-(match+un),7-match]
    return answer

q1_lottos = [44, 1, 0, 0, 31, 25]
q1_win_nums = [31, 10, 45, 1, 6, 19]

q2_lottos = [0, 0, 0, 0, 0, 0]
q2_win_nums = [38, 19, 20, 40, 15, 25]

print(solution(q1_lottos, q1_win_nums)) # [3, 5]
print(solution(q2_lottos, q2_win_nums)) # [1, 6]