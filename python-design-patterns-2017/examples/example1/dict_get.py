if 'owner' in roledict:
    owner = roledict['owner']
else:
    owner = admin


# Better

owner = roledict.get('owner', admin)


# By Brandon Rhodes
# http://rhodesmill.org/brandon/slides/2012-07-pyohio/
