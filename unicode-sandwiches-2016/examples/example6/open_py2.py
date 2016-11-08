#!/usr/bin/env python2
# -*- coding: utf-8 -*-

with open('file.txt', mode='r') as f:
    data = f.read()

print(type(data))
print(len(data))
print(data)

data_u = data.decode('utf8')
print(type(data_u))
print(len(data_u))
print(data_u)


# Use io.open

import io

with io.open('file.txt', mode='rt', encoding='utf8') as f:
    data = f.read()

print(type(data))
print(len(data))
print(data)
