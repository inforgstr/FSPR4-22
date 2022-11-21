def replace_exclamation(s):
    res = []
    for i in s:
        if i.lower() not in'aeiou':
            res.append(i)
        else:
            res.append('!')
    return ''.join(res)
print(replace_exclamation('Hwerrw'))