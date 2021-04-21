def anagrams(word, words):
    ans = words.copy()
    for w in words:
        if set(word) != set(w):
            ans.remove(w)
        else:
            for l in set(word):
                if word.count(l) != w.count(l):
                    ans.remove(w)
                    break
    return ans

print(
    anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
    # , ['aabb', 'bbaa'])
print(anagrams(
    'racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
    # , ['carer', 'racer'])
