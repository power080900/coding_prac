# 이진수 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return 하도록 함수를 작성하시오.
# 제한사항
# 이진수 bin1과 bin2의 길이는 1 이상 10 이하이다.
# 이진수 bin1과 bin2은 0을 제외하고 0으로 시작하지 않는다.

def solution(bin1,bin2):
    return bin(int('0b'+bin1,2)+int('0b'+bin2,2))[2:]

bin1,bin2 = '10','11'

print(solution(bin1,bin2)) # 101