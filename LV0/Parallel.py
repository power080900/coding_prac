# 점 네개의 좌표를 담은 이차원 배열 dots가 매개변수로 주어질 때, 두 직선이 평행이 되는 경우가 있으며 1 없으면 0을 return하는 함수를 작성하라.
# 제한 사항
# dots의 길이는 4이다.
# dots의 원소는 [x, y] 형식이며 정수이다.
# dots에 중복된 점은 없다.
# 두선이 겹쳐도 1을 return한다.
# 임의의 두 점을 이은직선이 x축 또는 y축과 평행한 경우는 없다

def solution(dots):
    answer = 0
    line1 = (dots[0][0]-dots[1][0]) / (dots[0][1]-dots[1][1])
    line2 = (dots[2][0]-dots[3][0]) / (dots[2][1]-dots[3][1])

    line3 = (dots[0][0]-dots[2][0]) / (dots[0][1]-dots[2][1])
    line4 = (dots[1][0]-dots[3][0]) / (dots[1][1]-dots[3][1])

    line5 = (dots[0][0]-dots[3][0]) / (dots[0][1]-dots[3][1])
    line6 = (dots[1][0]-dots[2][0]) / (dots[1][1]-dots[2][1])

    if line1 == line2 or line3 == line4 or line5 == line6:
        answer = 1
    return answer

print(solution([[1,4],[9,2],[3,8],[11,6]])) # 1