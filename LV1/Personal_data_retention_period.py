# 오늘 날짜를 의미하는 today, 약관의 유효기관을 담은 문자열 terms, 개인정보를 담은 privacies가 매개변수로 주어질 때,
# 파기해야하는 개인정보의 번호를 오름차순으로 정렬하여 return하도록 함수를 작성하시오.
# 제한사항
# today는"YYYY.MM.DD"형식의 문자열이다.
# terms의 길이는 1 이상 20 이하이며 "약관종류 유효기간"형식의 문자열이다.
# 약관 종류는 알파벳 대문자 하나이며 종류는 중복되지 않는다.
# 유효기간은 1 이상 100 이하의 자연수이다.
# privacies의 길이는 1 이상 100이하 이다.
# privacies[i]는 i+1번째 개인정보 수집일자와 약관 종류를 의미한다.
# privacies[i]의 날짜는 "YYYY.MM.DD"형식의 문자열이며 today 이전의 날짜만 주어진다.
# YYYY는 2000이상 2022이하의 자연수이다.
# MM은 01이상 12이하의 자연수이다.
# DD는 01이상 28이하의 자연수이다.
# 파기해야할 개인정보는 하나 이상이다.

def solution(today, terms, privacies):
    t_yy, t_mm, t_dd = map(int,today.split("."))
    t_days = t_yy * 12 * 28 + t_mm * 28 + t_dd
    answer = []
    for idx, privacy in enumerate(privacies):
        t, a = privacy.split(" ")
        yy, mm, dd = map(int,t.split("."))
        for term in terms:
            s, d = term.split(" ")
            d = int(d) + mm
            
            if s == a :
                p_days = yy * 12 * 28 + d * 28 + dd
                
        if t_days < p_days:
            pass
        else:
            answer.append(idx+1)
                    
    return answer

q1_today = "2022.05.19"
q1_terms = ["A 6", "B 12", "C 3"]
q1_privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(q1_today, q1_terms, q1_privacies)) # [1, 3]