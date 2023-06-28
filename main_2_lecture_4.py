from threading import Thread, Lock
import time


def bora(lock1, lock2):
    while True:
        print("Bora: Acquire Lock 1")
        lock1.acquire()
        print("Bora: Acquire Lock 2")
        lock2.acquire()
        print("Bora: Locks Acquired")
        lock1.release()
        lock2.release()
        print("Bora: Locks Released")
        time.sleep(0.5)


def burak(lock1, lock2):
    while True:
        print("Burak: Acquire Lock 2")
        lock2.acquire()
        print("Burak: Acquire Lock 1")
        lock1.acquire()
        print("Burak: Locks Acquired")
        lock2.release()
        lock1.release()
        print("Burak: Locks Released")
        print("")
        time.sleep(0.5)


# mutex is a common word (Mutual Exclusive)
if __name__ == "__main__":
    mutex1 = Lock()
    mutex2 = Lock()
    bora_thread = Thread(target=bora, args=(mutex1, mutex2))
    burak_thread = Thread(target=burak, args=(mutex1, mutex2))
    bora_thread.start()
    burak_thread.start()

    # inserting an infinite while loop, here comes the problem. indeed, one agent is waiting for the release,
    # but also the other thread is waiting for the release, so, the pc is stopped in this execution
    # if u run this algorithm, u'll see. it's called deadlock
    # dining philosophers is indeed a famous computer science problem that deals with this problem
    # there are 5 philosophers and 5 chopsticks. But a philosophers can be in two states: thinking or eating.
    # at the beginning all the philosophers are thinking. then, one philosophers decide to eat and get one chopstick
    # but he needs two chopsticks to eat. so he gets the chopstick at his left. but he needs two chopsticks!
