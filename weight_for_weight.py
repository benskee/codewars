def order_weight(strng):
    w = strng.split(" ")
    w_list = []
    for weight in w:
        w2 = 0
        for n in weight:
            w2 += int(n)
     
        w_list.append((weight, w2))
        w_list.sort(key=lambda x: x[1])
    for i in range(len(w_list)-1):
        for j in range(0, len(w_list)-i-1):
            if w_list[j][1] == w_list[j+1][1] and w_list[j][0] > w_list[j+1][0]:
                w_list[j], w_list[j+1] = w_list[j+1], w_list[j]
    ans = ''
    for tup in w_list:
        ans += tup[0] + " "
    return ans




print(order_weight("103 123 4444 99 2000"))
                #    "2000 103 123 4444 99")
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
                #    "11 11 2000 10003 22 123 1234000 44444444 9999")
print(order_weight(
    "71899703 200 6 91 425 4 67407 7 96488 6 4 2 7 31064 9 7920 1 34608557 27 72 18 81"))
#    '1 2 200 4 4 6 6 7 7 18 27 72 81 9 91 425 31064 7920 67407 96488 34608557 71899703')
print(order_weight(""))
#  "")
