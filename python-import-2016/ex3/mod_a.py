import time
import random
from threading import Thread

def worker():
    import mod_c
    time.sleep(random.randint(0, 3))
    my_counter = mod_c.COUNTER
    time.sleep(random.randint(0, 3))
    mod_c.COUNTER = my_counter + 1

ALL_THREADS = []

for i in range(10):
    t = Thread(target=worker)
    ALL_THREADS.append(t)
    t.start()
    #t.join()

[t.join() for t in ALL_THREADS]

import mod_c
print(mod_c.COUNTER)
