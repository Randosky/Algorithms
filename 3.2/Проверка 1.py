s = input()

res = 0
sub = ''
result = []
for char in s:
    if char not in sub:
        sub += char
        res = max(res, len(sub))
    else:
        cut = sub.index(char)
        sub = sub[cut + 1:] + char
    result.append(sub)

if len(result) == 0:
    print(1, s)
else:
    for substr in result:
        i = 0
        find = False
        while i <= len(s):
            if substr * i == s:
                find = True
                break
            i += 1
        if find:
            print(i, substr)
            break