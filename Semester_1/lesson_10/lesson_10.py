# a, b, *args = (2, 3, 4, 5, 5, 6, 7, 4)
# print(a, b, args)

# for i in range(10):
#     print(i)

# print("Next range")
# for i in range(3, 10):
#     print(i)


# print('Next range')
# for i in range(3, 10, 2):
#     print(i)




info = []
info.append({
    'name': 'asda',
    'age': 12,
})
for i in range(len(info)*2):
    print(info)






# info = []
# d = input()
# s = int(input())
# info.append({
#     'name': d,
#     'age': s
# })
# for i in range(len(info)):
#     print(info*10)






# # continue / break / pass
# num = [1, 2, 3, 4, 5, 6, 7]
# for val in num:
#     if val == 5 or val == 7:
#         print(f"пропустить {val}")
#         continue # -> for 
#     print('val =', val)


# continue / break / pass
num = [1, 2, 3, 4, 5, 6, 7]
for val in num:
     if val == 5 or val == 7:
         print(f"пропустить {val}")
         break # -> for 
     print('val =', val)
# if 1==1:
#     pass
