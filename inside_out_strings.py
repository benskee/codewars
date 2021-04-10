def inside_out(st):
    w_list = st.split(" ")
    nw_list = []
    for w in w_list:
        if len(w) == 1:
            nw_list.append(w)
        elif len(w)%2 == 0:
            center = len(w)//2
            w1 = w[:center]
            w2 = w[center:]
            nw_list.append(w1[::-1]+w2[::-1])
            
        else:
            center = len(w)//2
            w1 = w[:center]
            w2 = w[center+1:]
            nw_list.append(w1[::-1] + w[center] + w2[::-1])
    ans = ""
    for w in nw_list:
        ans += w + " "
    return ans[:-1]



print(inside_out('man i need a taxi up to ubud'))
                #    'man i ende a atix up to budu')
print(inside_out('what time are we climbing up the volcano'))
                #    'hwta item are we milcgnib up the lovcona')
print(inside_out('take me to semynak'))
                #    'atek me to mesykan')
