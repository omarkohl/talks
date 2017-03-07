class _Singleton:
    pass

singleton = _Singleton()





# Other module
from pkg1.mod1 import singleton

singleton.make_connection()  # etc.



# Problem 'singleton' can not be intercepted (e.g. with @property) if
# something needs to be changed.
