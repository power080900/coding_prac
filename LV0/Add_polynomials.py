# 덧셈으로 이뤄진 다항식이 polynomial의 매개변수로 주어질때 동류항 끼리 더한 결과를 문자열로 return하는 함수를 작성하시오.
# polynomial에 있는 수는 0 초과 100미만이다.
# polynomial의 변수는 "x"만 존재한다.
# polynomial은 양의 정수, 공백, 'x', '+'로만 이뤄져있다.
# 공백은 연속되지 않으며 시작과 끝에는 없다
# 문자와 숫자 사이의 곱하기는 생략한다
# polynomial은 일차항과 상수만 존재한다.
# 계수 1은 생략한다.
# 상수항이 제일 마지막에 온다.
# polynomial[i]는 0 초과 50 미만이다.

def solution(polynomial):
    pn = polynomial.split(' + ')
    x = 0
    n = 0
    for i in pn:
        if i[-1] == 'x':
            if i[0] != 'x':
                x += int(i[:-1])
            else:
                x += 1
        else:
            n += int(i)
    
    if x == 0 and n == 0:
        return '0'
    elif x == 0:
        return str(n)
    elif x == 1:
        if n == 0:
            return 'x'
        else:
            return 'x + ' + str(n)
    elif n == 0:
        return str(x) + 'x'
    else:
        return str(x) + 'x + ' + str(n)
    
print(solution("3x + 7 + x")) # 4x + 7