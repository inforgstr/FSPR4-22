import time

file = open("doc.txt", "r")


start = time.perf_counter()

text = file.readlines()
mes = ""
i = 0
while len(text) > i:
    mes += f"In {i+1} line: {len(text[i])}\n"
    i += 1

print(mes + f"{time.perf_counter()-start:8f}")
