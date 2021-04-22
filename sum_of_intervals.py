def sum_of_intervals(intervals):
    def length(i):
        return len(range(i[0], i[1]))
    ans = 0

    def check_ranges(int_list):
        int_list = sorted(int_list, key=lambda i: i[0])
        for x in range(0, len(int_list)-1):
            if int_list[x+1][0] >= int_list[x][0] and int_list[x+1][0] <= int_list[x][1]:
                if int_list[x+1][1] < int_list[x][1]:
                    int_list.remove(int_list[x+1])
                    return int_list
                else:
                    int_list.append((int_list[x][0], int_list[x+1][1]))
                    int_list.remove(int_list[x])
                    int_list.remove(int_list[x])
                    return int_list
        return int_list
    while intervals:
        if len(intervals) == len(check_ranges(intervals)):
            break
        else:
            intervals = check_ranges(intervals)
    for x in intervals:
        ans += length(x)
    return ans




print(sum_of_intervals([(1, 5)]))
# , 4)
print(sum_of_intervals([(1, 5), (6, 10)]))
# , 8)
print(sum_of_intervals([(1, 5), (1, 5)]))
# , 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
# , 7)
print(sum_of_intervals([(-478, -217), (13, 373), (-172, 92), (-226, -23), (395, 492), (73, 198), (93, 181), (482, 489), (-241, 56),
                        (-493, -204)]))
# print(sum_of_intervals([(-478, -217), (13, 373), (-172, 92), (-226, -23), (395, 492), (73, 198), (93, 181), (482, 489), (-241, 56),
#                         (36, 181), (-396, -124), (352, 357), (109, 474), (220, 269), (119, 482), (-164, 459), (-127, 14), (-47, 328), (269, 311), (-493, -204)]))
