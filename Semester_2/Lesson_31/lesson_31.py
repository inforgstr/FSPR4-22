# from PIL import Image, ImageFilter

# # array = [1,2,3,4,5,6,7,8,9,10]


# # def fn(item):
# #     return str(item > 5)


# # def group_by(fn, array):
# #     a = {fn(item) for item in array}

# #     d = {}

# #     for el in array:
# #         if fn(el) not in d:
# #             d[fn(el)] = []
# #         if fn(el) in a:
# #             d[fn(el)].append(el)

# #     return d


# # print(group_by(fn, array))

# with Image.open("Semester_2/Lesson_31/pokemone.jpg") as img:
#     img.load()

# # img.save("path", "format png, jpg, jpeg")
# # print(img.filter(ImageFilter.EDGE_ENHANCE).show())
# # print(img.convert())

# # resized = img.resize((200, 200))

# # print(resized.filter(ImageFilter.CONTOUR).show())
# print(img.crop((50, 50, 300, 300)).show())
