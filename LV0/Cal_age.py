# 정수 year과 나이 종류를 나타내는 age_type이 매개변수로 주어질때 2030년에 몇살인지 return하도록 함수를 작성하시오.
# 제한사항
# year는 1950 이상 2030 이하 정수이다.
# age_type은 "Korea" 또는 "Year"이다.

def solution(year, age_type):
    if age_type == "Korea":
        return 2030 - year + 1
    else:
        return 2030 - year
    
q1_year = 2000
q1_age_type = "Korea"

print(solution(q1_year, q1_age_type)) # 31
