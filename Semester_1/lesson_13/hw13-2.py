def values_none(lists):
    a = {}
    for i in lists:
        a[i] = None
    return a

l = ['qwerty', 'none', 'useful']
print(values_none(l))