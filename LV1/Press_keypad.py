# 순서대로 누를 숫자가 담긴 배열 numbers와 선호하는 손을 나타내는 hand가 매개변수로 주어질 때,
# 각 번호를 누른 손가락이 왼손인지 오른손인지를 나타내는 연속된 문자열 형태로 return하도록 함수를 작성하시오.
# 제한사항
# numbers 배열의 크기는 1 이상 1,000 이하입니다.
# numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
# hand는 "left" 또는 "right"입니다.
# 왼손 엄지는 "*", 오른손 엄지는 "#"에서 시작합니다.
# 1,4,7은 왼손으로 3,6,9는 오른손으로 누릅니다.
# 2,5,8,0을 누를 때, 더 가까운 손이 먼저 움직이며, 두 엄지손가락 거리가 같다면 hand에 따라 누릅니다.

def solution(numbers, hand):
    mat = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,2]]
    l_now = 10
    r_now = 11
    answer = ''
    for num in numbers:
        if num in [1,4,7]:
            l_now = num
            answer += "L"
        elif num in [3,6,9]:
            r_now = num
            answer += "R"
        else:
            l_dis_x,l_dis_y = mat[l_now]
            r_dis_x,r_dis_y = mat[r_now]
            dis_x, dis_y = mat[num]
            l_dis = abs(l_dis_x-dis_x)+abs(l_dis_y-dis_y)
            r_dis = abs(r_dis_x-dis_x)+abs(r_dis_y-dis_y)
            if l_dis > r_dis:
                r_now = num
                answer += "R"
            elif r_dis > l_dis:
                l_now = num
                answer += "L"
            elif r_dis == l_dis:
                if hand == "right":
                    r_now = num
                    answer += "R"
                elif hand == "left":
                    l_now = num
                    answer += "L"
    return answer

q1_numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
q1_hand = "right"

q2_numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
q2_hand = "left"

print(solution(q1_numbers,q1_hand)) # "LRLLLRLLRRL"
print(solution(q2_numbers,q2_hand)) # "LRLLRRLLLRR"