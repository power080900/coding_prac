# 직원 n 명이 설정한 출근 희망시각을 담은 schedule배열과 일주일 동안 출근 시각을 담은 2차원 배열 timelog, 
# 이벤트 시작요일을 의미하는 startday가 매개변수로 주어질 때, 상품을 받을 직원의 수를 return하는 함수를 작성하시오.
# 제한사항
# n과 schedule의 길이는 1 이상 1,000 이하이다.
# schedule[i]는 i번째 직원이 설정한 시각을 의미하며 700 이상 1100 이하의 자연수이다.
# timelog의 길이는 1 이상 1,000 이하이다.
# timelog[i]의 길이는 7이다.
# timelog[i][j]는 i+1번째 직원이 이벤트 j+1일차에 출근한 시각을 의미하며 600 이상 2359 이하의 자연수이다.
# startday는 1 이상 7 이하의 자연수이다.
# startday의 1은 월요일 7은 일요일을 의미한다.
# 일주일동안 출근희망시각+10이내에 출근한 직원에게 상품을 증정한다.
# 토요일, 일요일은 출근 희망시각 이후 출근해도 이벤트에 영향을 미치지 않는다.

def solution(schedule, timelog, startday):
    answer = 0
    for i, time in enumerate(schedule):
        time_hh = time // 100
        time_mm = time % 100
        check_time = time + 10
        if time_mm + 10 >= 60:
            check_time = (time_hh + 1) * 100 + (time_mm + 10) % 60
        check = 0
        for j in range(7):
            time_log = timelog[i][j]
            if (j+startday)%7 not in [6,0] and time_log <= check_time:
                check += 1
        if check == 5:
            answer += 1
    return answer

q1_schedule = [700, 800, 1100]
q1_timelog = [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]]
q1_startday = 5

q2_schedule = [730, 855, 700, 720]
q2_timelog = [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]]
q2_startday = 1

print(solution(q1_schedule, q1_timelog, q1_startday)) # 3
print(solution(q2_schedule, q2_timelog, q2_startday)) # 2