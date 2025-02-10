# 가습기 모드를 나타낸 문자열 mode_type과 습도를 나타낸 정수 humidity, 설정값을 나타낸 정수 val_set이 주어질때 현재 가습기가 몇단계인지 return하는 함수를 작성하시오.
# 제한사항
# mode_type은 "auto", "target", "minimum"이있다
# 가습량은 0 ~ 5단계로 구분된다.
# humidity와 valset은 0이상 100이하 정수이다.
# auto모드는 0 ~ 10일 때 습도 5단계 10 ~ 20일 때 4단계 20 ~ 30일 때 3단계 30 ~ 40일 때 2단계 40 ~ 50일 때 1단계 50이상일 때 0단계이다.
# target모드는 설정값 미만일 경우 3단계, 설정값 이상일 경우 1단계이다.
# minimum모드는 설정값 미만일 경우 1단계, 설정값 이상일 경우 0단계이다.

def func1(humidity, val_set):
    if humidity < val_set:
        return 3
    return 1

def func2(humidity):
    if humidity >= 50:
        return 0
    if humidity >= 40:
        return 1
    if humidity >= 30:
        return 2
    if humidity >= 20:
        return 3
    if humidity >= 10:
        return 4
    return 5

def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 0

def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity)
    elif mode_type == "target":
        answer = func1(humidity, val_set)
    elif mode_type == "minimum":
        answer = func3(humidity, val_set)
    return answer

q1_type = "auto"
q1_humidity = 23
q1_val_set = 45
q2_type = "target"
q2_humidity = 41
q2_val_set = 40
q3_type = "minimum"
q3_humidity = 10
q3_val_set = 34

print(solution(q1_type, q1_humidity, q1_val_set)) # 3
print(solution(q2_type, q2_humidity, q2_val_set)) # 1
print(solution(q3_type, q3_humidity, q3_val_set)) # 1