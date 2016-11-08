#!/usr/bin/env python3

with open('file.txt', mode='rt', encoding='utf-8') as f:
    text = f.read()

print(type(text))
print(text)

text2 = "是一種針對Unicode的可變長度字元編碼，也是一种前缀码\n"

with open('file2.txt', mode='wt', encoding='utf-8') as f:
    f.write(text2)
