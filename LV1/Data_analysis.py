# 정렬한 데이터가 담긴 data와 정보를 뽑아낼 기준이 담긴 ext, 기준값 val_ext, 정렬기준 sort_by가 매개변수로 주어질 때,
# sort_by에 해당하는 기준에 따라 오름차순 정렬하여 return하는 함수를 작성하시오.
# 제한사항
# data의 길이는 1 이상 500 이하이다.
# data[i]의 원소는 [code, date, maximum, remain]형식 이다
# code는 1 이상 100,000 이하의 자연수이다.
# 제조일은 20000101 이상 29991231 이하이다.
# data[i][1]은 yyyymmdd 형태 값을 가지며 올바른 날짜만 가진다.
# maximum은 1 이상 10,000 이하이며, remain은 1 이상 최대수량 이하이다.
# ext와 sort_by는 "code", "date", "maximum", "remain" 중 하나이다.
# val_ext는 ext에 따라 올바른 범위의 숫자로 주어진다.



def solution(data, ext, val_ext, sort_by):
    answer = data.copy()

    if ext == "code":
        num = 0
    elif ext == "date":
        num = 1
    elif ext == "maximum":
        num = 2
    elif ext == "remain":
        num = 3

    for i in data:
        if i[num] > val_ext:
            answer.remove(i)
    
    if sort_by == "code":
        sort_num = 0
    elif sort_by == "date":
        sort_num = 1
    elif sort_by == "maximum":
        sort_num = 2
    elif sort_by == "remain":
        sort_num = 3

    answer.sort(key=lambda x: x[sort_num])
    return answer

q1_data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
q1_ext = "date"
q1_val_ext = 20300501
q1_sort_by = "remain"

print(solution(q1_data, q1_ext, q1_val_ext, q1_sort_by)) # [[3,20300401,10,8],[1,20300104,100,80]]