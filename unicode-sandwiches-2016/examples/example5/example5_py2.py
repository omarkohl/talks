#!/usr/bin/env python2
# -*- coding: utf-8 -*-

var1 = u"I am a ünicôde string"
var2 = "I am bytes"
var3 = ''.join(chr(i) for i in [70, 80, 90, 100, 110])

print(type(var1))
print(type(var2))
print(type(var3))

print(list(var1))
print(list(var2))
print(list(var3))

print(type(var1.encode('utf8')))
print(type(var2.decode('utf8')))
print(type(var3.decode('utf8')))
print(var3.decode('utf8'))
