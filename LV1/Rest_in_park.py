# 돗자리들의 한 변의 길이가 담긴 정수 리스트 mats와 공원의 2차원 자리 배치도 park가 매개변수로 주어질 때,
# 깔 수 있는 가장 큰 돗자리 한변의 길이를 return 하도록 함수를 작성하시오.
# 제한사항
# mats의 길이는 1 이상 10 이하이다.
# mats[i]는 1 이상 20 이하이다.
# park의 길이는 1 이상 50 이하이다.
# park[i]의 길이는 1 이상 50 이하이다.
# park[i][j]는 문자열이며 사람이 있다면 알파벳으로 표시되고 없다면 "-1"로 표시된다.
# 사람이 앉아있는 부분에는 돗자리를 깔 수 없다.
# 깔 수 있는 가장 큰 돗자리 한변의 길이가 없다면 -1을 return한다.

def solution(mats, park):
    mats.sort(reverse = True)
    H, W = len(park), len(park[0])
    dp = [[0] * W for _ in range(H)]
    max_size = 0
    answer = -1
    if mats[-1] > H or mats[-1] > W:
        return answer
    else:
        for i in range(H):
            for j in range(W):
                if park[i][j] == "-1":
                    if i == 0 or j == 0 :
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_size = max(max_size, dp[i][j])

        if max_size < mats[-1]:
            return answer
        else:
            for mat in mats:
                if max_size >= mat:
                    return mat
                
q1_mats = [5,3,2]
q1_park = [["A", "A", "-1", "B", "B", "B", "B", "-1"], 
           ["A", "A", "-1", "B", "B", "B", "B", "-1"], 
           ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], 
           ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], 
           ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], 
           ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]

print(solution(q1_mats, q1_park)) # 3
