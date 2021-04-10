def digital_root(n):
    while n > 9:
        y = 0
        for l in str(n):
            m = int(l)
            y += m
            n = y
    return n


print(digital_root(16))
#  7)
print(digital_root(942))
#  6)
print(digital_root(132189))
#  6)
print(digital_root(493193))
#  2)
