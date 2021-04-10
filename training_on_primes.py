def prime_factors(n):
    print(n)
    x = 2
    p_list = []
    a_list = []
    ans = ''
    while n >= x:
        if n % x == 0:
            n = n/x
            p_list.append(x)
            if x not in a_list:
                a_list.append(x)
        else:
            x += 1
    p_list.append(int(n))
    for num in a_list:
        c = p_list.count(num)
        if c == 1:
            ans += f"({num})"
        else:
            ans += f"({num}**{c})"

    return ans

print(prime_factors(7775460))
#  "(2**2)(3**3)(5)(7)(11**2)(17)")
