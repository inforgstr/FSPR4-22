file = open("doc_1.txt", "w")
lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

for line in range(len(lst)):
    file.write(lst[line]+"\n")
