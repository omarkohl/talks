#!/usr/bin/env python3

encodings = [
    'latin1',
    'cp1252',
    'cp437',
    'iso8859-2',
    'iso8859-3',
    'iso8859-4',
    'iso8859-5',
    #'iso8859-6',  # undefined character
    'iso8859-7',
    #'iso8859-8',  # undefined character
    'iso8859-9',
    'iso8859-10',
    'iso8859-11',
    #'iso8859-12',  # ISO 8859-12 was abandoned
    'iso8859-13',
    'iso8859-14',
    'iso8859-15',
    'iso8859-16',
    ]

for encoding in encodings:
    with open('file.txt', mode='rt', encoding=encoding) as f:
        print('Encoding %s, Content: %s' % (encoding, f.read()))

with open('file.txt', mode='rb') as f:
    print(list(f.read()))
