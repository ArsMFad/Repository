import os

target = "Hello, World!"
target = list(target)
start = ""

for t in range(len(target)):
    sym = 32
    while chr(sym) != target[t]:
        os.system("cls")
        sym += 1
        print (start + (chr(sym)))
    start += chr(sym)

# It is useless, but fun :3
