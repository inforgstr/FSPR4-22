def func_matrix(a, b):
    matrix = []
    for i in range(b):
        arr = []
        for j in range(a):
            arr.append(j)
        matrix.append(arr)
    return matrix

a = 3
b = 4
print(func_matrix(a, b))