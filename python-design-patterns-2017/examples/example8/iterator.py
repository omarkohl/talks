# Example by Brandon Rhodes
# http://rhodesmill.org/brandon/slides/2012-07-pyohio/

class Box(object):
    def __init__(self):
        self.things = [10, 20, 30]
    def __iter__(self):
        return BoxIterator(self)

class BoxIterator(object):
    def __init__(self, box):
        self.box = box
        self.index = -1

    def next(self):
        self.index += 1
        if self.index >= len(self.box.things):
            raise StopIteration()
        return self.box.things[self.index]


# Or


class Box(object):
    def __init__(self):
        self.things = [10, 20, 30]

    def __iter__(self):
        for thing in things:
            yield thing
