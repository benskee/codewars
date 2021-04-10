def list_squared(m, n):
    ans = []
    for num in range(m, n):
        f_list = [] 
        f_tot = 0
        for fact in range(1, int(num**.5)+1):
            if num%fact == 0:
                f_list.append(fact)
                f_list.append(num//fact)
        for number in set(f_list):
            f_tot += number**2
        if f_tot**.5 == int(f_tot**.5):
            if num == 1:
                ans.append([1,1])
            else:
                ans.append([num, f_tot])

    return ans

print(list_squared(1, 250))
#  [[1, 1], [42, 2500], [246, 84100]])
print(list_squared(1, 43))
print(list_squared(42, 250))
#  [[42, 2500], [246, 84100]])
print(list_squared(250, 500))
#  [[287, 84100]])

