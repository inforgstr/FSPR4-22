def cakes(recipe, available):
    a = []
    v = []
    result = []
    for i in recipe.values():
        a.append(i)
    for si in available.values():
        v.append(si)
    counter = 0
    for i in range(len(a)):
        if i <= len(a)+1:
            if len(a) <= len(v):
                if i <= counter:
                    res = v[counter] // a[counter]
                    result.append(res)
                if v[counter] < a[counter]:
                    return 0
        counter += 1
        i += 1
    return result      

recipe = {'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
available = {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000, 'cream': 5000}
print(cakes(recipe, available))