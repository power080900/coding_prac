# storage에는 물건의 이름이 num에는 물건의 개수가 적혀있다. 
# clean_stroage와 clean_num에 넣어주고 정리된 창고에서 개수가 가장 많은 물건을 return하는 함수를 작성하라
# 제한사항
# storage와 num은 같으며 길이는 1 이상 30 이하이다.
# stroage[i]는 영어 대소문자로 이루어져있으며 대소문자를 구분한다.
# storage[i]의 길이는 1 이상 30 이하이다.
# num[i]는 1 이상 20 이하이다.

def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            clean_num.append(num[i])
    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer

print(solution(["pencil", "pencil", "pencil", "book"], [2,4,3,1])) # pencil