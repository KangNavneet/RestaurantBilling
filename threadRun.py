import time
from threading import Thread

class worker(Thread):
    def run(self):
        for x in range(0,11):
            print(x)
            time.sleep(1)


class waiter(Thread):
    def run(self):
        for x in range(100,103):
            print("Hello!")
            time.sleep(5)

def run():
    worker().start()
    waiter.start()

x=run()