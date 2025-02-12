# 동영상 길이를 나타내는 문자열 video_len, 기능 수행 전 위치를 나타내는 pos, 오프닝 시작을 나타내는 op_start, 오프닝 끝을 나타내는 op_end, 
# 사용자 입력을 나타내는 commands가 매개변수로 주어질 때, 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return하는 함수를 작성하시오.
# 제한사항
# video_len, pos, op_start, op_end은 "mm:ss" 형식의 길이 5의 문자열이다.
# mms과 ss는 0 이상 59 이하인 정수이다.
# commands의 길이는 1 이상 100 이하이다.
# commands의 원소는 "next" 또는 "prev"이다.
# next는 현재 위치에서 10초 후의 위치로 이동한다.
# prev는 현재 위치에서 10초 전의 위치로 이동한다.
# 오프닝은 op_start부터 op_end까지이다.
# 현재 재생위치가 오프닝 구간에 포함되어 있으면 오프닝 구간의 끝으로 이동한다.
# 현재 재생위치가 10초 미만일 경우 prev 명령어를 입력해도 0초로 이동한다.
# 현재 위치에서 동영상의 남은 시간이 10초 미만일 경우 next 명령어를 입력해도 동영상의 끝으로 이동한다.

def solution(video_len, pos, op_start, op_end, commands):
    now = int(pos[:2])*60 + int(pos[3:])
    op_s_time = int(op_start[:2])*60 + int(op_start[3:])
    op_e_time = int(op_end[:2])*60 + int(op_end[3:])
    vi_t_time = int(video_len[:2])*60 + int(video_len[3:])
    
    now = op_e_time if op_s_time <= now <= op_e_time else now
    
    for command in commands:
        if command == "next":
            now = min(now + 10, vi_t_time)
        elif command == "prev":
            now = max(now - 10, 0)
        
        now = op_e_time if op_s_time <= now <= op_e_time else now
    
    return f"{now // 60:02d}:{now % 60:02d}"

video_len = "34:33"
pos = "13:00"
op_start = "00:55"
op_end = "02:55"
commands = ["next", "prev"]

print(solution(video_len, pos, op_start, op_end, commands)) # "13:00"