def replace_exclamation(s):
    res = []
    for i in s:
        if i.lower() not in'aeiou':
            res.append(i)
        else:
            res.append('!')
    return ''.join(res)
print(replace_exclamation('Hwerrw'))

# code of second task codewars
def solve(s):
    lowers = []
    uppers = []
    for i in s:
        if i.lower() == i:
            lowers.append(i)
        else:
            uppers.append(i)
    if len(lowers) == len(uppers) or len(lowers) > len(uppers):
        return s.lower()
    elif len(lowers) < len(uppers):
        return s.upper()
print(solve('GooFDl'))