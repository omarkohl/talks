import sys
from pprint import pprint

print('\n\n')
pprint(sys.modules)

import mod_b

print('\n\n')
pprint(sys.modules)

print('\n\n')
print(
    "sys.modules['mod_b']: %r\nid: %s\ntype: %s" % (
        sys.modules['mod_b'],
        id(sys.modules['mod_b']),
        type(sys.modules['mod_b']),
        )
    )
print('\n\n')
print(
    "mod_b: %r\nid: %s\ntype: %s" % (
        mod_b,
        id(mod_b),
        type(mod_b),
        )
    )

print('\n\n')
print("dir -> sys.modules['mod_b']: %s" % dir(sys.modules['mod_b']))
