# 공원을 나타내는 문자열 park와 로봇 강아지가 수행할 명령이 담긴 routes가 매개변수로 주어질 때, 모든 명령 수행 후 위치를 [x,y]로 return 하도록 함수를 작성하시오.
# 제한사항
# park의 길이는 3 이상 50 이하이다.
# park[i]의 길이는 3 이상 50 이하이다.
# park[i]는 "S", "O", "X" 문자열로 이뤄져 있으며 "S"는 시작위치, "X"는 장애물, "O"는 이동가능한 위치를 의미한다.
# routes의 길이는 1 이상 50 이하이다.
# routes[i]는 "op n"의 형태로 이뤄져있으며 op는 방향, n은 이동할 칸의 수를 의미한다.
# op는 "N", "E", "S", "W" 중 하나이다.
# n은 1 이상 9 이하의 자연수이다.
# 로봇 강아지가 장애물을 만나거나 공원의 끝부분에 도달하면 해당 명령은 무시하고 다음 명령을 수행한다.

def solution(park, routes):
    loc = [-1,-1]
    lh, lw = len(park), len(park[0])
    way = {'E':(0,1), 'N':(-1,0), 'W':(0,-1), 'S':(1,0)}
    
    for idx,p in enumerate(park):
        if p.find('S') != -1 : 
            loc = [idx, p.find('S')]
        
    pre_loc = loc.copy()
    for route in routes:
        op, n = route.split(' ')
        n = int(n)
        
        loc[0] += way[op][0]*n
        loc[1] += way[op][1]*n
        
        if not(0<=loc[0]<lh and 0<=loc[1]<lw) : 
            loc = pre_loc.copy(); 
            continue
        
        if (op=='W' or op=='E'):
            min_loc,max_loc = min(pre_loc[1],loc[1]), max(pre_loc[1],loc[1])
            if 'X' in park[loc[0]][min_loc:max_loc+1]:
                loc = pre_loc.copy()
    
        else : 
            is_X = False
            min_loc,max_loc = min(pre_loc[0],loc[0]), max(pre_loc[0],loc[0])
            for p in park[min_loc:max_loc+1]:
                if p[loc[1]] == 'X': is_X = True; break
            
            if is_X : 
                loc = pre_loc.copy(); 
                continue
        
        pre_loc = loc.copy()
        
    return loc
    
q1_park = ["SOO","OOO","OOO"]
q1_routes = ["E 2","S 2","W 1"]

print(solution(q1_park, q1_routes)) # [2, 1]