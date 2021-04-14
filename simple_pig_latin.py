def pig_it(text):
    ans = ''
    for w in text.split(" "):
        if w in "!.?":
            ans += w
        elif len(w) == 1:
            ans += w + 'ay '
        else:
            ans += w[1:] + w[0] + 'ay '
    return ans.strip()


print(pig_it('Pig latin is cool'))
#  'igPay atinlay siay oolcay')
print(pig_it('This is my string'))
#  'hisTay siay ymay tringsay')
