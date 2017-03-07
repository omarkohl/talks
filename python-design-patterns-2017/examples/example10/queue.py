# Example from Alex Martelli
# http://www.aleax.it/goo_pydp.pdf

class Queue:
    ...
    def put(self, item):
        self.not_full.acquire()
        try:
            while self._full():
                self.not_full.wait()
                self._put(item)
                self.not_empty.notify()
        finally:
            self.not_full.release()
    ...

# https://hg.python.org/cpython/file/3.4/Lib/queue.py


class LifoQueue(Queue):
    def _put(self, item):
        self.queue.appendleft(item)
