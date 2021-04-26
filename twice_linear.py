def dbl_linear(n):
    ans = [1]
    trip = []
    c = 0

    def ln(num, ans):
        x = (ans[num]*2)+1
        ans.append(x)
        trip.append((ans[num]*3)+1)
        while x >= trip[0]:
            ans.append(trip[0])
            trip.pop(0)
    while len(ans) < (4*n):
        ln(c, ans)
        c += 1
    ans = list(set(ans))
    ans.sort()
    return ans[n]




print(dbl_linear(10))
# , 22)
print(dbl_linear(20))
# , 57)
print(dbl_linear(30))
# , 91)
print(dbl_linear(50))
# , 175)
