def format_duration(seconds):
    if not seconds:
        return "now"
    y1=d1=h1=m1=s1= ""
    y = int(seconds/31536000)
    d = int(seconds/86400 % 365)
    h = int(seconds/3600 % 24)
    m = int(seconds/60 % 60)
    s = seconds % 60
    if y > 0 and y <2:
        y1 = "1 year, "
    elif y > 1:
        y1 = f"{y} years, "
    if d > 0 and d <2:
        d1 = "1 day, "
    elif d > 1:
        d1 = f"{d} days, "
    if h > 0 and h <2:
        h1 = "1 hour, "
    elif h > 1:
        h1 = f"{h} hours, "
    if m > 0 and m <2:
        m1 = "1 minute, "
    elif m > 1:
        m1 = f"{m} minutes, "
    if s > 0 and s <2:
        s1 = "1 second, "
    elif s > 1:
        s1 = f"{s} seconds, "

    ans = y1+d1+h1+m1+s1
    ans = ans[:-2]
    if "," in ans:
        ans = ans[::-1].replace(",","dna ",1)
        ans = ans[::-1]
    return ans



print(format_duration(1))
# , "1 second")
print(format_duration(62))
# , "1 minute and 2 seconds")
print(format_duration(120))
# , "2 minutes")
print(format_duration(3600))
# , "1 hour")
print(format_duration(3662))
# , "1 hour, 1 minute and 2 seconds")
print(format_duration(132030240))
# , "4 years, 68 days, 3 hours and 4 minutes")
