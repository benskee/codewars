def bowling_score(frames):

    bonus_list = []
    total = 0
    if frames[-3] != ' ':
        bonus = frames[-1]
        if bonus == 'X' or bonus == '/':
            total += 10
        else:
            total += int(bonus)
        frames = frames[:-1]

    for roll in frames:
        if roll == ' ':
            a_frames = frames.replace(roll, '')
    for roll in range(len(a_frames)-2):

        if a_frames[roll] == 'X' and a_frames[roll+2] == '/':
            bonus_list.append('10')
        elif a_frames[roll] == 'X':
            bonus_list.append(a_frames[roll+1])
            bonus_list.append(a_frames[roll+2])
        elif a_frames[roll] == '/':
            bonus_list.append(a_frames[roll+1])
    for roll in bonus_list:
        if roll == 'X':
            total += 10
        elif roll == '/':
            total += 10
        else:
            total += int(roll)

    frame_list = frames.split()

    for frame in frame_list:

        if frame == 'XX':
            total += 20
        elif frame == 'X':
            total += 10
        elif frame[1] == '/':
            total += 10
        else:
            total += int(frame[0]) + int(frame[1])

    return total

print(bowling_score('11 11 11 11 11 11 11 11 11 11'))
print(bowling_score('X X X X X X X X X XXX'))
print(bowling_score('00 5/ 4/ 53 33 22 4/ 5/ 45 XXX'))
