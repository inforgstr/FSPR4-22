# def domain_name(url):
#     """
#     5-kyu
#     """
#     if url.startswith("www"):
#         f = url[url.index(".")+1 :]
#         return f[: f.index(".")]
#     else:
#         if "https" in url:
#             return url[8:][: url[8:].index(".")]
#         elif "http" in url:
#             f = url[7:]
#             return url[7:][: url[7:].index(".")]
#         return url[: url.index(".")]


# print(domain_name("google.com"))
# import time

# data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]

# def data_reverse(data):
#     """
#     6-kyu
#     """
#     start = time.perf_counter()
#     return [mc for x in [data[x-7: x+1] for x in range(len(data)) if (x+1)%8==0][::-1] for mc in x], f"{time.perf_counter()-start:8f}"

# print(data_reverse(data1))

# b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
# c = ["A", "B", "C", "D"]


# def stock_list(list_of_art: list[str], list_of_cat: list[str]):
#     """
#     https://www.codewars.com/kata/54dc6f5a224c26032800005c
#     6-kyu
#     """
#     dct = {x: 0 for x in list_of_cat}

#     for category in list_of_cat:
#         for art in list_of_art:
#             if art.startswith(category):
#                 art = art.split(" ")[1]
#                 if category in dct:
#                     dct[category] += int(art)
#                 else:
#                     dct[category] = int(art)

#     if list(dct.values()).count(0) == len(dct):
#         return ""

#     res = [
#         f"({list_of_cat[l]} : {dct[list_of_cat[l]]})" for l in range(len(list_of_cat))
#     ]

#     return " - ".join(res)


# print(stock_list(b, c))


# def delete_nth(order: list[int],max_e: int):
#     """
#     https://www.codewars.com/kata/554ca54ffa7d91b236000023
#     6-kyu
#     """
#     i = len(order)-1

#     while i >= 0:
#         if order.count(order[i]) > max_e:
#             order.pop(i)
#         i -= 1
#     return order

# print(delete_nth([20,37,20, 20, 21], 1))


# def dashatize(n: int):
#     if not isinstance(n, int):
#         return None
#     s = str(n)
    
#     res = []
#     for i in range(len(s)):
#         new = ""
#         for j in range(len(s)):
#             if int(s[i]) % 2 == 0:
#                 new += s[i]
#                 continue
#             else:
#                 res.append(s[i])
#                 break
#         res.append(new)
    
    # for i in range(len(s)):
    #     if i == len(s) - 1 and int(s[i]) % 2 == 0:
    #         continue
    #     if i == len(s) - 1:
    #         res.append(s[i])
    #     else:
    #         if int(s[i]) % 2 == 0 and int(s[i+1]) % 2 == 0:
    #             res.append(s[i]+s[i+1])
    #         elif int(s[i])%2!=0 or (int(s[i])%2==0 and i == 0):
    #             res.append(s[i])

#     return res

# print(dashatize(86320))
