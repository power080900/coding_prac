# 알람이 울리는 횟수를 센 시간을 나타내는 정수 h1, m1, s1, h2, m2, s2가 주어질 때,
# 알람이 울리는 횟수를 반환하는 함수를 작성하시오
# 제한사항
# 초침이 시침이나 분침과 겹쳐질 때 알람의 횟수를 세야하며 시침과 분침에 동시에 겹쳐질 때는 한 번만 센다.
# 초침이 시침이나 분침과 겹쳐지는 경우는 없다.
# 0 <= h1, h2 <= 23
# 0 <= m1, m2 <= 59
# 0 <= s1, s2 <= 59
# h1시 m1분 s1초부터 h2시 m2분 s2초까지 알람이 울리는 횟수를 세야 한다.
# h1, m1, s1은 h2, m2, s2보다 항상 작다.
# 시간이 23시 59분 59초를 넘어가는 경우는 없다.

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    t1 = h1*3600 + m1*60 + s1
    t2 = h2*3600 + m2*60 + s2
    for i in range(t1,t2):
        h_angle = (i%43200)/43200*360
        m_angle = (i%3600)/3600*360
        s_angle_1 = (i%60)/60*360
        s_angle_2 = (i%60+1)/60*360
        now_h_t = i//3600
        now_m_t = i%3600 // 60
        now_s_t = i%60
        now  = [now_h_t, now_m_t, now_s_t]
        
        if now == [0,0,0] or now == [12,0,0]:
            answer += 1
        elif now == [11,59,59] or now == [23,59,59]:
            if i == t2-1:
                answer += 1
            else:
                pass
        elif h_angle == m_angle and m_angle == s_angle_1:
            answer += 1
        elif s_angle_1 < h_angle < s_angle_2:
            if s_angle_1 < m_angle < s_angle_2:
                answer += 2
            else:
                answer += 1
        elif not s_angle_1 < h_angle < s_angle_2:
            if s_angle_1 < m_angle < s_angle_2:
                answer += 1
        elif not s_angle_1 < m_angle < s_angle_2:
            if s_angle_1 < h_angle < s_angle_2:
                answer += 1

    return answer

# q1_h1, q1_m1, q1_s1, q1_h2, q1_m2, q1_s2 = 11,59,30,12,0,0
q2_h1, q2_m1, q2_s1, q2_h2, q2_m2, q2_s2 = 0,0,0,23,59,59

# print(solution(q1_h1, q1_m1, q1_s1, q1_h2, q1_m2, q1_s2)) # 2
print(solution(q2_h1, q2_m1, q2_s1, q2_h2, q2_m2, q2_s2)) # 1