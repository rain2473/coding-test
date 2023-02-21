def solution(m, musicinfos):
    answer, play_time = '', 0
    m = change(m)
    for musicinfo in musicinfos:
        time1, time2, name, melody = musicinfo.split(",")
        time1, time2 = time1.split(":"), time2.split(":")
        time = (int(time2[0]) - int(time1[0])) * 60 + (int(time2[1]) - int(time1[1]))
        melody = change(melody)
        melody = melody * (time//len(melody) + (time%len(melody)!=0))
        melody = melody[:time]
        if m in melody and time > play_time:
            answer = name
            play_time = time
    if answer == "":
        answer = "(None)"
    return answer

def change(m):
    scale = {"C#":"c","D#":"d","F#":"f","G#":"g","A#":"a"}
    for a,b in scale.items():
        m = m.replace(a,b)
    return m