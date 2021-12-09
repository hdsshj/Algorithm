# 입력
#   네오가 기억하는 멜로디를 담은 문자열 m
#   방송된 곡의 정보를 담고 있는 배열 musicinfos
# 처리
#
# 출력
#   
import math

def replace_string (m) :
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

def solution(m, musicinfos):
    answer = None
    max_play_time = 0
    m = replace_string(m)
    for musicinfo in musicinfos:
        start_time, end_time, name, melody = musicinfo.split(',')
        play_time = int(end_time[:2]) * 60 + int(end_time[3:]) - int(start_time[:2]) * 60 + int(start_time[3:])
        melody = replace_string(melody)
        # 올림(실행시간 / 멜로디길이)
        melody_count = math.ceil(play_time / len(melody))
        melody_played = (melody * melody_count)[:play_time]
        
        # max_play_time 끼면 80점, 빼면 90점
        # 문제점 찾아야함
        if m in melody_played and play_time > max_play_time:
            answer = name
            max_play_time = play_time
    if answer is None :
        return "(None)"
    
    return answer