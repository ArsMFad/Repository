import os

target = ["H", "e", "l", "l", "o", ",", " ", "W", "o", "r", "l", "d", "!"]
start = ""


for t in range(len(target)):
    sym = 0
    while chr(sym) != target[t]:
        os.system("cls")
        sym += 1
        print (start + (chr(sym)))
    start += chr(sym)
