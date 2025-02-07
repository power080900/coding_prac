# num1과 num2를 입력받아 두 수가 같으면 1 다르면 -1을 출력하는 프로그램을 작성하시오.
# 제한 사항
# num1과 num2는 0 이상 10000 이하의 수

def solution(num1, num2):
    return 1 if num1 == num2 else -1

if solution(5, 3) == -1:
    print('pass')