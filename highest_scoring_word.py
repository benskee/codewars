def high(x):
    w_list = x.split(" ")
    num = 0
    ans = ""
    for w in w_list:
        x = 0
        for l in w:
            x += ord(l)-96
            if x > num:
                ans = w
                num = x
    return ans

print(high('man i need a taxi up to ubud'))
#  'taxi')
print(high('what time are we climbing up the volcano'))
#  'volcano')
print(high('take me to semynak'))
#  'semynak')
