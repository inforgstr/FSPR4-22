"""
Максимальное расстояние

Расстояние между двумя двоичными строками равно сумме их длин после удаления общего префикса. 
Например: общий префикс 1011000и 1011110так 1011расстояние len("000") + len("110") = 3 + 3 = 6.

Учитывая список двоичных строк, выберите пару, которая дает вам максимальное расстояние среди всех возможных пар, и верните это расстояние.
"""


# def max_distance(prefix_1, prefix_2):
#     max_d = ""
#     min_length = min(len(prefix_1), len(prefix_2))
#     for i in range(min_length):
#         if prefix_1[i]==prefix_2[i]:
#             continue
#         else:
#             max_d += prefix_1[i:] + prefix_2[i:]
#             break

#     return len(max_d)


# print(max_distance(prefix_1, prefix_2))

import time


def email_reciever(emails):
    """
    Unique Email Addresses
    """
    start = time.perf_counter()

    adresess = []

    for email in emails:
        if "+" in email[: email.index("@")]:
            email = (
                "".join(email[: email.index("+")].split("."))
                + email[email.index("@") :]
            )
        else:
            email = (
                "".join(email[: email.index("@")].split("."))
                + email[email.index("@") :]
            )

        adresess.append(email)

    return len(set(adresess)), f"{time.perf_counter()-start:8f} ms"


print(email_reciever(["test.email+alex@leetcode.com", "test.email@leetcode.com"]))

# emails = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]

# def valid_emails(emails):
#             v_email = ''
#             v_emails = []
#             if len(emails) > 100: return 'Error'
#             for email in emails:
#                 if len(email) > 100: continue
#                 if email[0] == '+' or email[0] == '@': continue
#                 if email[email.index('@', 1) + 1: -4] == "": continue
#                 if email[-4:] != '.com': continue
#                 if '@' in email[email.index('@', 1) + 1::]: continue
        
#                 for i in range(len(email)):
#                     if email[i] == '+' or email[i] == '@':
#                         i = email.index('@', 1)
#                         v_email += email[i:]
#                         break
#                     elif email[i] == '.':
#                         continue
#                     else:
#                         v_email += email[i]
                    
#                 v_emails.append(v_email)
#                 v_email = ''
                        
#             return v_emails

# v = valid_emails(emails)
# count = 0
# for i in range(len(v)):
#     if v[i] in v[i+1::] : continue
#     else: count += 1
#     print(v[i])
# print(count)
