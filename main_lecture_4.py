from threading import Thread, Lock


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def earn(self):
        for _ in range(10_000_000):
            self.lock.acquire()
            self.balance += 1
            # this operation has three sub operations ... get, increase, assign.
            # these sub-operations should be atomic, so, they can not be divided
            # all these three sub operations should use a LOCK, saying to other
            # threads to wait, to do not to anything. After the thread finishes
            # its job, it releases the lock, so, now, other threads can do their
            # job. so now, we will modify this code using locks
            self.lock.release()
        print("Earned\n")

    def spend(self):
        for _ in range(10_000_000):
            self.lock.acquire()
            self.balance -= 1
            self.lock.release()
        print("Spent")

    def get_balance(self):
        return self.balance


if __name__ == "__main__":
    bank_account = BankAccount()
    # bank_account.earn()
    thread1 = Thread(target=bank_account.earn, args=())
    thread1.start()
    # bank_account.spend()
    thread2 = Thread(target=bank_account.spend, args=())
    thread2.start()
    thread1.join()
    thread2.join()
    # so, two sub-threads, one for spend and earn method
    # using 1_000_000 in the for loop, I find that the balance is 44_204, a clear error!
    # using instead 1_000 in the for loop, I find that the balance is 0 (w/o locks)
    # using Lock, acquire and release encapsulating the operation, we will obtain as a result 0
    current_balance = bank_account.get_balance()
    print(current_balance)
