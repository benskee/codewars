def move_zeros(array):
    x = array.count(0)
    arr = []
    for n in array:
        if n != 0:
            arr.append(n)
    while x > 0:
        arr.append(0)
        x -= 1
    return arr



print(move_zeros(
    [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
    # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
print(move_zeros(
    [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
    # [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
