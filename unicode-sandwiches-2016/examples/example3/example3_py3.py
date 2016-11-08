#!/usr/bin/env python3

encodings = ['utf_8', 'utf_16', 'utf_16le', 'utf_16be', 'utf_32']

my_str = "One \U0001D11E costs 22 €\n"

for encoding in encodings:
    with open('file_' + encoding + '.txt', mode='wt', encoding=encoding) as f:
        f.write(my_str)

print(len(my_str))
print(my_str)
