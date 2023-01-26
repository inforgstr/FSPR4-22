DATA = [
    "user",
    "password",
]

legals = ["am", "good"]
illegals = ["monster", "bad"]


def replacer(lyric, legals="", illegals=""):
    res = lyric.split()
    s = []
    for i in range(len(res)):
        if "," not in res[i] and "." not in res[i] and "!" not in res[i]:
            s.append(res[i])
            s.append(" ")
        elif "," in res[i]:
            s.append(res[i][:-1])
            s.append(", ")
        elif "." in res[i]:
            s.append(res[i][:-1])
            s.append(". ")
        elif "!" in res[i]:
            s.append(res[i][:-1])
            s.append("! ")

    for i in range(len(s)):
        if s[i].lower() in illegals:
            s[i] = len(s[i]) * "*"
        elif s[i].lower() in legals:
            s[i] = s[i].upper()
    return "".join(s)


login = input("Input your login: ")
password = input("Input your password: ")

if login == DATA[0] and password == DATA[1]:
    print("You have succesfully loged in!")
    chat = input("Input a text here: ")
    print(replacer(chat, legals, illegals))
else:
    print("Please try again!")
