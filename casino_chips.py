def solve(arr):
    sorted_list = sorted(arr, reverse=True)
    if sorted_list[0] > sorted_list[1] + sorted_list[2]:
        return sorted_list[1] + sorted_list[2]
    elif sorted_list[0] == sorted_list[1] and sorted_list[0] == sorted_list[2]:
        return int(sorted_list[0]*1.5)
    else:
        return sorted_list[0] + ((sorted_list[1] + sorted_list[2] - sorted_list[0])//2)


print(solve([1, 1, 1]))
print(solve([1, 2, 1]))
print(solve([4, 1, 1]))
print(solve([8, 2, 8]))
print(solve([8, 1, 4]))
print(solve([7, 4, 10]))
print(solve([12, 12, 12]))
print(solve([1, 23, 2]))
