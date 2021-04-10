def generate_hashtag(s):
    if not s: return False
    j = '#' + s.replace(" ", '')
    if len(j) > 139:
        return False
    else:
        return j


print(generate_hashtag(''))
print(generate_hashtag('Do We have A Hashtag'))
print(generate_hashtag('Codewars'))
print(generate_hashtag('Codewars      '))
print(generate_hashtag('Codewars Is Nice'))
print(generate_hashtag('codewars is nice'))
print(generate_hashtag('CodeWars is nice'))
print(generate_hashtag('c i n'))
print(generate_hashtag('codewars  is  nice'))
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))