def snail(snail_map):
    x = True
    ans =[]
    while len(snail_map)>0:
        if x == True:
            for a in snail_map[0]:
                ans.append(a)
            snail_map.pop(0)
            for b in range(0, len(snail_map)):
                ans.append(snail_map[b][-1])
                snail_map[b].pop(-1)
            x = False
        else:
            for a in snail_map[-1][::-1]:
                ans.append(a)
            snail_map.pop(-1)
            for b in range(1, len(snail_map)):
                ans.append(snail_map[-b][0])
                snail_map[-b].pop(0)
            x = True
    return ans
    







array1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
# expected1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(snail(array1))


array2 = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
# expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(snail(array2))

array3 =    [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]
# expected = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
print(snail(array3))
