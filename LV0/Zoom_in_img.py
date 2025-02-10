# 그림을 나타낸 문자열 배열 picture과 정수 k가 매개변수로 주어질때 k배 확대된 그림을 나타내는 문자열배열을 return하는 함수를 작성하시오.
# 제한사항
# picture의 길이는 1 이상 20 이하이다.
# picture[i]의 길이는 1 이상 20 이하이다.
# picture[i]는 '.'과 'x'로 이뤄져 있다
# k는 1 이상 10 이하이다.

def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            temp = ''
            for j in range(len(picture[i])):
                temp += picture[i][j] * k
            answer.append(temp)

    return answer

q1_picture = [".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]
q1_k = 2
q2_picture = ["x.x", ".x.", "x.x"]
q2_k = 3

print(solution(q1_picture, q1_k)) # ["..xxxx......xxxx..", "..xxxx......xxxx..", "xx....xx..xx....xx", "xx....xx..xx....xx", "xx......xx......xx", "xx......xx......xx", "..xx..........xx..", "..xx..........xx..", "....xx......xx....", "....xx......xx....", "......xx..xx......", "......xx..xx......", "........xx........", "........xx........"]
print(solution(q2_picture, q2_k)) # ["xxx...xxx", "xxx...xxx", "xxx...xxx", "...xxx...", "...xxx...", "...xxx...", "xxx...xxx", "xxx...xxx", "xxx...xxx"]