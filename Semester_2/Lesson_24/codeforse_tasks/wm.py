# n = int(input())

# for i in [input() for _ in range(n)]:
#     if len(i) > 10:
#         print(i[0] + str(len(i)-2) + i[-1])
#     else:
#         print(i)

# n = int(input())



def command(n):
    return map(lambda x: 1 if x.count('0') < 2 else 0, [input() for x in range(n)])




# print(list(command(n)).count(1))

def next_match(s: str) -> int:
    string = s.split(" ")
    new = input().split(" ")

    for i in range(int(string[0])):
        if i < int(string[1]):
            yield new[i]
        
        elif new[i-1] == new[i]:
            yield new[i]
        else:
            break

# s = input()
# answer = list(next_match(s))

# print(len(answer) - answer.count('0'))
