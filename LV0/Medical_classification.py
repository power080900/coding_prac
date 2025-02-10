# 환자의 코드를 나타내는 문자열 code가 매개변수로 주어질 때, 환자에 맞는 병과를 return 하도록 함수를 작성하시오.
# 제한사항
# code의 길이는 4 이상 20 이하이다.
# code는 알파벳 소문자와 숫자 "_"로만 이뤄져있다.
# 분류 기준은 "_eye"로 끝나면 "Ophthalmolgy", "head"로 끝나면 "Neurosurgery", "infl"로 끝나면 "Orthopedics", "skin"으로 끝나면 "Dermatology" 그 외의 경우는 "direct recommendation"을 출력한다.

def solution(code):
    if code.endswith("_eye"):
        return "Ophthalmolgy"
    elif code.endswith("head"):
        return "Neurosurgery"
    elif code.endswith("infl"):
        return "Orthopedics"
    elif code.endswith("skin"):
        return "Dermatology"
    else:
        return "direct recommendation"
    
q1_code = "dry_eye"
q2_code = "pat23_08_20_head"

print(solution(q1_code)) # Ophthalmolgy
print(solution(q2_code)) # Neurosurgery