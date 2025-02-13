# 택배상자의 개수를 나타내는 정수 n, 가로로 놓는 상자의 개수를 나타내는 정수 w, 꺼내려는 상자의 번호를 나타내는 정수 num이 주어질 때, 꺼내야 하는 상자의 총개수를 return하는 함수를 작성하시오.
# 제한사항
# n은 2 이상 100 이하이다.
# w는 1이상 10 이하이다.
# num은 1 이상 n 이하이다.
# 상자를 쌓는 방법은 첫 줄은 왼쪽에서 오른쪽으로 w개를 쌓고 다음 줄은 오른쪽에서 왼쪽으로 w개를 쌓는 방식으로 진행된다.

def solution(n, w, num):
    warehouse = []
    stack = []
    
    for i in range(n):
        if len(warehouse) % 2 == 0:
            stack.append(i + 1)
        else:
            stack.insert(0, i + 1)
        
        if len(stack) == w:
            warehouse.append(stack)
            stack = []

    if stack:
        while len(stack) < w:
            if len(warehouse) % 2 == 0:
                stack.append(0)
            else:
                stack.insert(0, 0)
        warehouse.append(stack)

    for i in range(len(warehouse)):
        for j, value in enumerate(warehouse[i]):
            if value == num:
                if warehouse[-1][j] == 0:
                    return len(warehouse) - i - 1
                return len(warehouse) - i

q1_n = 22
q1_w = 6
q1_num = 8

q2_n = 13
q2_w = 3
q2_num = 6

print(solution(q1_n, q1_w, q1_num)) # 3
print(solution(q2_n, q2_w, q2_num)) # 4
        
