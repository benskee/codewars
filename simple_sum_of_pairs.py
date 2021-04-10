def solve(n):
    if n < 10:
        return n
    num_len = len(str(n))
    a = "".join('9'*(num_len-1))
    b = n - (int(a))
    num_str = sorted(a) + sorted(str(b))
    ans = 0
    for num in num_str:
        ans += int(num)

    return ans





# 29 16  18
# 28 17   18
# 27 18   18
# 26 19   18

# 25 20   9
# 24 21
# 23 22
# 30 15
# 31 14

# 999 141

# 6999 20

print(solve(18))
print(solve(29))
print(solve(45))
print(solve(1140))
print(solve(7019))
