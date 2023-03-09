file = open("doc_1.txt", "w")
lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

for item in lst:
    file.write(item+"\n")
