def get_participants(handshakes):
    x = 0 
    y = 0
    while y < handshakes:
        x += 1 
        y += x
    return x+1



print(get_participants(0))
#  1)
print(get_participants(1))
#  2)
print(get_participants(3))
#  3)
print(get_participants(6))
#  4)
print(get_participants(7))
#  5)
