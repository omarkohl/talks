class _Singleton:
    pass

_singleton = _Singleton()


def get_singleton():
    return _singleton




# Other module
from pkg1.mod1 import get_singleton 

singleton = get_singleton()
singleton.make_connection()  # etc.


# Recommended approach by Brandon Rhodes
# http://rhodesmill.org/brandon/slides/2012-07-pyohio/
