def mix(s1, s2):
    ans = []
    for x in range(97,123):
        s1c = s1.count(chr(x))
        s2c = s2.count(chr(x))
        if s1c > 1 or s2c > 1:
            if s1c > s2c:
                ans.append(f"1:{s1c*chr(x)}/")
            elif s2c > s1c:
                ans.append(f"2:{s2c*chr(x)}/")
            else:
                ans.append(f"=:{s1c*chr(x)}/")
    ans.sort()
    ans.sort(reverse=True, key=lambda x: len(x))
    ans = "".join(ans)[:-1]


    return ans



print(mix("Are they here", "yes, they are here"))
                #    "2:eeeee/2:yy/=:hh/=:rr")
print(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"))
#                     #    , '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
# print(mix("looping is fun but dangerous", "less dangerous than coding"))
#                 #    "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
# print(mix(" In many languages", " there's a pair of functions"))
#                 #    "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
# print(mix("Lords of the Fallen", "gamekult"))
#                 # , "1:ee/1:ll/1:oo")
# print(mix("codewars", "codewars"))
#                 # , "")
# print(mix("A generation must confront the looming ", "codewarrs"))
#                     #    , "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")
