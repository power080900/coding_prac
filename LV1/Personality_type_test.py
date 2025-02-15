# 질문을 판단하는지표가 담긴 survey와 각 질문에 대한 답변이 담긴 choices가 주어질 때, 사용자의 성격 유형을 return하도록 함수를 작성하시오.
# 제한사항
# survey(=n)의 길이는 1 이상 1,000 이하이다.
# survey의 원소는 "RT", "TR", "CF", "FC", "JM", "MJ", "AN", "NA" 중 하나이다.
# choices의 길이는 survey의 길이와 같다.
# choices의 원소는 1 이상 7 이하이다.
# 


def solution(survey, choices):
    answer = ''
    dicts = {'T' : 0, 'R' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    for i in range(len(survey)) : 
        if choices[i] - 4 < 0: 
            dicts[survey[i][0]] += 4 - choices[i]
        elif choices[i] - 4 > 0:
            dicts[survey[i][1]] += choices[i] - 4
    answer += 'R' if dicts['R'] >= dicts['T'] else 'T'
    answer += 'C' if dicts['C'] >= dicts['F'] else 'F'
    answer += 'J' if dicts['J'] >= dicts['M'] else 'M'
    answer += 'A' if dicts['A'] >= dicts['N'] else 'N'
    return answer

q1_survey = ["AN", "CF", "MJ", "RT", "NA"]
q1_choices = [5, 3, 2, 7, 5]

q2_survey = ["TR", "RT", "TR"]
q2_choices = [7, 1, 3]

print(solution(q1_survey, q1_choices)) # "TCMA"
print(solution(q2_survey, q2_choices)) # "RCJA"