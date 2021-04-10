def race(v1, v2, g):
    d = v2 - v1
    f = d/3600
    t = g/f

    if t < 0:
        return None
    s = int(t%60)
    m = int((t%3600)/60)
    h = int(t/3600)
    return [h, m, s]



print(race(720, 850, 70))
#  [0, 32, 18])
print(race(80, 91, 37))
#  [3, 21, 49])
print(race(820, 81, 550))
#  None)
