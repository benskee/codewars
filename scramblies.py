def scramble(s1, s2):

    s_set = set(s1)
    for s in s_set:
        if s1.count(s) < s2.count(s):
            return False

    return True



    

# print(scramble('rkqodlw', 'world'))
# print(scramble('cedewaraaossoqqyt', 'codewars'))
# print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))
print(scramble('oowqoowjadiyawiiazr', 'wajsrorywgqdy'))
