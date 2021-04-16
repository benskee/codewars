def make_readable(seconds):
    h = int(seconds/3600)
    m = int(seconds/60 % 60)
    s = seconds % 60
    # if h < 10:
    #     h = f"0{str(h)}"
    # else:
    #     h = str(h)
    # if m < 10:
    #     m = f"0{str(m)}"
    # else:
    #     m = str(m)
    # if s < 10:
    #     s = f"0{str(s)}"
    # else:
    #     s = str(s)
    ans = f"{h}:{m}:{s}"
    return ans




print(make_readable(0))
#  "00:00:00")
print(make_readable(5))
#  "00:00:05")
print(make_readable(60))
#  "00:01:00")
print(make_readable(86399))
#  "23:59:59")
print(make_readable(359999))
#  "99:59:59")
