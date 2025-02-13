# 바탕화면 상태를 나타내는 배열 wallpaper가 매개변수로 주어질 때,
# 바탕화면 파일들은 한번에 드래그하는 최소한의 이동거리를 담은 시작점과 끝점을 정수배열로 return 하는 함수를 작성하시오.
# 제한사항
# 드래그 시작점을 lux, luy, 끝점을 rdx, rdy라고 할 때 [lux, luy, rdx, rdy]를 return한다.
# wallpaper의 길이는 1 이상 50 이하이다.
# wallpaper[i]는 1 이상 50 이하인 정수이다.
# wallpaper[i][j]는 i+1행 j+1열을 의미한다.
# wallpaper[i][j]는 "#" 또는 "."으로 이루어져 있다.
# lux < rdx, luy < rdy를 만족한다.

def solution(wallpaper):
    x_pile = []
    y_pile = []
    for x, row in enumerate(wallpaper):
        for y, point in enumerate(row):
            if point == "#":
                x_pile.append(x)
                y_pile.append(y)
    lux = min(x_pile)
    luy = min(y_pile)
    rdx = max(x_pile)
    rdy = max(y_pile)
    answer = [lux,luy,rdx+1,rdy+1]
    return answer

q1_wallpaper = [".#...", "..#..", "...#."]
q2_wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]

print(solution(q1_wallpaper)) # [0, 1, 3, 4]
print(solution(q2_wallpaper)) # [0, 0, 7, 9]