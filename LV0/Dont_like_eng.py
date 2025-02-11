# 문자열 nubmers가 매개변수로 주어질때 정수로 바꿔 return하는 함수를 작성하시오.
# 제한사항
# numbers는 소문자로 구성되어있으며 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'들이 공백없이 조합되어있다.
# numbers의 길이는 1 이상 50 이하이다.
# 'zero'는 맨 앞에 올 수 없다.

def solution(numbers):
    nums = {"0":"zero",
            "1":"one",
            "2":"two",
            "3":"three",
            "4":"four",
            "5":"five",
            "6":"six",
            "7":"seven",
            "8":"eight",
            "9":"nine"}
    for i, j in zip(nums.values(),nums.keys()):
        numbers = numbers.replace(i,j)
    return int(numbers)

q1 = "onetwothreefourfivesixseveneightnine"
q2 = "onefourzerosixseven"

print(solution(q1)) # 123456789
print(solution(q2)) # 14067