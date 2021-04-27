def rot13(message):
    ans = ''
    for l in message:
        if ord(l) > 64 and ord(l) < 91:
            if ord(l) + 13 > 90:
                ans += chr(65 + (ord(l)+13-91))
            else:
                ans += chr(ord(l)+13)
        elif ord(l) > 96 and ord(l) < 123:
            if ord(l) + 13 > 122:
                ans += chr(97 + (ord(l)+13-123))
            else:
                ans += chr(ord(l)+13)
        else:
            ans += l
    return ans


# 97-122
# 65-90
print(rot13("test"))
print(rot13("Test"))
print(rot13("Codewars"))
print(rot13("Avoid success at all costs"))
