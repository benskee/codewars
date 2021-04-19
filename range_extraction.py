def solution(args):
    y = []
    ans = ''

    def check_y(y, x):
        ans = ''
        if y:
            if len(y) > 2:
                ans += "," + (f'{y[0]}-{y[-1]}')
            else:
                ans += "," + (str(y[0]))
                ans += "," + (str(y[1]))
        else:
            ans += "," + (str(args[x]))
        return ans

    for x in range(len(args)-1):
        if args[x] == args[x+1]-1:
            y.append(args[x])
            y.append(args[x+1])
        else:
            ans += check_y(y, x)
            y = []
    ans += check_y(y, -1)

    return ans[1:]




print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9,
                10, 11, 14, 15, 17, 18, 19, 20]))
                            #   '-6,-3-1,3-5,7-11,14,15,17-20')
print(
    solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
    #  '-3--1,2,10,15,16,18-20')
