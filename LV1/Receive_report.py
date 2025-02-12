# 이용자 ID가 담긴 문자열 배열 id_list,와 각 신고한 이용자 정보가담긴 report, 정지 기준 신고횟수 k가 주어질 때, 
# 각 유저별로 처리결과 메일을 받은 횟수를 배열에 담아 return 하도록 함수를 작성하시오.
# 제한사항
# id_list의 길이는 2 이상 1,000 이하이다.
# id_list[i]의 길이는 1 이상 10 이하이며 알파벳 소문자로만 이루어져 있다.
# report의 길이는 1 이상 200,000 이하이다.
# report[i]의 길이는 3 이상 21 이하이다.
# report[i]는 ["A B"] 형태이며 A는 이용자, B는 신고한 이용자를 의미한다.
# k는 1 이상 200 이하의 자연수이다.
# k번 이상 신고된 이용자는 정지되며, 이용자를 신고한 유저에게 정지사실을 메일로 발송한다.

def solution(id_list, report, k):
    count = {i:0 for i in id_list}
    result = {i:[] for i in id_list}
    mail_count = {i:0 for i in id_list}
    
    for i in set(report):
        a, b = i.split(' ')
        count[b] += 1
        result[b].append(a)
    
    for i,item in count.items():
        if item >= k:
            for j in result[i]: mail_count[j] += 1
            
    return [i for i in mail_count.values()]

q1_id_list = ["muzi", "frodo", "apeach", "neo"]
q1_report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
q1_k = 2

q2_id_list = ["con", "ryan"]
q2_report = ["ryan con", "ryan con", "ryan con", "ryan con"]
q2_k = 3

print(solution(q1_id_list, q1_report, q1_k)) # [2, 1, 1, 0]
print(solution(q2_id_list, q2_report, q2_k)) # [0, 0]