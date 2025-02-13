# 1등부터 마지막까지 현재 등수 순서대로 담긴 문자열 players와 해설진이 부른 이름을 담은 배열 callings가 매개변수로 주어질 때,
# 경주가 끝났을 때 1등부터 마지막까지 순서대로 담긴 배열을 return하도록 함수를 작성하시오.
# 제한사항
# players의 길이는 5 이상 50,000 이하이다.
# players[i]는 i번째 선수의 이름을 의미하며 알파벳 소문자들로만 이루어진 문자열이다.
# players[i]의 길이는 3 이상 10 이하이다.
# callings의 길이는 2 이상 1,000,000 이하이다.
# 경주 중 현재 1등의 이름은 불리지 않는다.

def solution(players, callings):
    ranks = {player: i for i, player in enumerate(players)}
    
    for call in callings:
        win_rank = ranks[call]
        if win_rank == 0:
            continue
        
        lose_rank = win_rank - 1
        lose_player = players[lose_rank]
        
        ranks[call], ranks[lose_player] = lose_rank, win_rank
        players[lose_rank], players[win_rank] = call, lose_player

    return players

q1_players = ["mumu", "soe", "poe", "kai", "mine"]
q1_callings = ["kai", "kai", "mine", "mine"]

print(solution(q1_players, q1_callings)) # ["mumu", "kai", "mine", "soe", "poe"]