# 버스에는 좌석이 seat의 갯수만큼 있으며 각 정거장에서 승/하차한 정보 'passengers'가 주어질때 A가 버스에 탑승한 순간 빈좌석의 수는 몇개인지 return 하는 함수를 작성하시오.
# 제한사항
# seat는 1 이상 30 이하인 자연수이다.
# passengers는 1 이상 10 이하의 자연수이다.
# passengers[i]는 1이상 20 이하의 자연수이다.
# passengers의 길이가 n이면 A는 n+1번째에서 버스에 탑승한다.
# passengers[i]의 길이는 모두 동일하며 원소는 'On', 'Off'또는 '-'이다.
# 'On'은 승차, 'Off'는 하차, '-'는 의미없음을 의미한다.

def func1(num):
    if 0 > num:
        return 0
    else:
        return num

def func2(num):
    if 0 > num:
        return 0
    else:
        return num

def func3(station):
    num = 0
    for people in station:
        if people == 'Off':
            num += 1
    return num

def func4(station):
    num = 0
    for people in station:
        if people == 'On':
            num += 1
    return num

def solution(seat, passengers):
    pass_num = 0
    for station in passengers:
        pass_num += func4(station)
        pass_num -= func3(station)
    answer = func1(seat - pass_num)
    return answer

print(solution(10, [["On", "On", "On", "On", "On", "On", "On", "On", "-", "-"], ["On", "On", "Off", "Off", "Off", "On", "On", "-", "-", "-"], ["On", "On", "On", "Off", "On", "On", "On", "Off", "Off", "Off"], ["On", "On", "Off", "-", "-", "-", "-", "-", "-", "-"]])) # 0