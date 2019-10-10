import queue
import random
import time


def shu_line():
    buy_parson = []
    q = queue.Queue()

    for i in range(100):
        q.put('parson' + str(i))

    kaien = time.time() + 5
    now = time.time()
    while now < kaien and not q.empty():
        now = time.time()
        time.sleep(random.randint(0, 1))
        buy_parson.append(q.get())

    print(buy_parson)


shu_line()
