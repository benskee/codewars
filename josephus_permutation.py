def josephus(items,k):
    if not items: return items
    
    a_list = []
    i = 0
   
    while len(items) or k == 1:
        x = len(items)
        if i + k <= x and items:
            x = len(items)
            a_list.append(items.pop(i+k-1))
            i += k-1
            print(a_list)
        elif i + k > x and items:
            # print(i)
            # print(k)
            # print(x)
            x = len(items)
            a_list.append(items.pop((i+k-1) % x))
            i = (i + k-1) % x
            print(a_list)
            print('test')
        else:
            break

    return a_list






print(josephus([1,2,3,4,5,6,7,8,9,10],1))
print(josephus([1,2,3,4,5,6,7,8,9,10],2))
# print(josephus(["C","o","d","e","W","a","r","s"],4))
# print(josephus([1,2,3,4,5,6,7],3))