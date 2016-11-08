#!/usr/bin/env python3
import os

text = "Exämple text\n"

# Try to encode and write to file and catch error

try:
    text.encode('ascii')
except UnicodeEncodeError as exx:
    print("Error while encoding ASCII " + str(exx))

with open('output_ascii.txt', mode='wt', encoding='ascii') as f:
    try:
        f.write(text)
    except UnicodeEncodeError as exx:
        print("Error while writing ASCII file " + str(exx))


# Special error handling

error_handling = [
    'ignore',
    'replace',
    'xmlcharrefreplace'
    ]
for eh in error_handling:
    result = text.encode('ascii', errors=eh)
    print('Text with "errors=%s": ' % eh + result.decode('ascii'))


# UnicodeDecodeErrors

# Write random bytes to a file
with open('binary.dat', mode='wb') as f:
    f.write(os.urandom(20))

# Decode the file as UTF-8. This will most likely fail.
try:
    with open('binary.dat', mode='rt', encoding='utf-8') as f:
        print(f.read())
except UnicodeDecodeError:
    print("The file could not be decoded as UTF-8. Maybe try opening it with another encoding?")


# Mojibake (aka Gremlins)
data = "Français"
data_b = data.encode('utf-8')
data2 = data_b.decode('cp1252')
print("\n\nExample of Mojibake: " + data2)
