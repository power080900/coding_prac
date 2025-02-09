# 아이디와 패스워드가 담긴 id_pw와 회원정보가 담긴 db가 주어질 때, 로그인 성공/실패에 따른 메세지를 .return하는 함수를 작성하시오.
# 제한사항
# 아이디와 패스워드가 일치하는 정보가 있으면 "login"을 return한다.
# 아이디만 일치하면 "fail"을, 아이디는 일치하지만 비밀번호가 틀리다면 "wrong pw"를 return한다.
# 아이디은 소문자와 숫자로 이뤄진 문자열이다.
# 비밀번호는 숫자로 구성된 문자열이다.
# 회원들의 비밀번호는 동일할 수 있지만 아이디는 같을 수 없다.
# id_pw의 길이는 2이다
# id_pw와 db의 원소는 [아이디, 패스워드]형태이다.
# id의 길이는 1 이상 15 이하이다.
# pw의 길이는 1 이상 6 이하이다.
# db의 길이는 1 이상 10 이하이다.
# db의 원소의 길이는 2이다.

def solution(id_pw, db):
    answer = ""
    for db_id, db_pw in db:
        if id_pw[0] == db_id:
            if id_pw[1] == db_pw:
                answer = "login"
            else:
                answer = "wrong pw"
            break
        else:
            answer = "fail"
    return answer

q1_id_pw = ["meosseugi", "1234"]
q1_db = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]
q2_id_pw = ["programmer01", "15789"]
q2_db = [["programmer02", "111111"],["programmer00", "134"], ["programmer01", "1145"]]
q3_id_pw = ["rabbit04", "98761"]
q3_db = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]

print(solution(q1_id_pw, q1_db)) # login
print(solution(q2_id_pw, q2_db)) # wrong pw
print(solution(q3_id_pw, q3_db)) # fail