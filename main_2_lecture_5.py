import random
import time
from threading import Semaphore, Thread

# with respect to the previous file, now, we use Semaphore class


class DiningPhilosophers:
    def __init__(self, number_of_philosophers=5, meal_size=7):
        """[7 7 7 7 7]"""
        self.meals = [meal_size for _ in range(number_of_philosophers)]
        self.chopsticks = [Semaphore(value=1) for _ in range(number_of_philosophers)]
        '''
        from 1 -> 0, if someone tries to use a resource and he finds a value of 0 -> -1 but
        the semaphore can not get negative values, so, wait
        Semaphore(value=1) means that the resource can be used only once
        '''
        self.status = ['  T  ' for _ in range(number_of_philosophers)]
        self.chopstick_holders = ['     ' for _ in range(number_of_philosophers)]

    def philosopher(self, i):
        j = (i + 1) % 5
        while self.meals[i] > 0:
            self.status[i] = '  T  '
            time.sleep(random.random())
            self.status[i] = '  _  '
            if self.chopsticks[i].acquire(timeout=1):
                self.chopstick_holders[i] = ' /  '
                time.sleep(random.random())
                if self.chopsticks[j].acquire(timeout=1):
                    self.chopsticks[j].acquire()
                    self.chopstick_holders[i] = ' /\  '
                    self.status[i] = '  E  '
                    time.sleep(random.random())
                    self.meals[i] -= 1
                    self.chopsticks[i].release()
                    self.chopstick_holders[i] = ' /  '
                self.chopsticks[i].release()
                self.chopstick_holders[i] = '    '
                self.status[i] = '  T  '


def main():
    n = 5
    m = 7
    dining_philosophers = DiningPhilosophers(n, m)
    philosophers = [Thread(target=dining_philosophers.philosopher, args=(i,)) for i in range(n)]
    for philosopher in philosophers:
        philosopher.start()
    while sum(dining_philosophers.meals) > 0:
        print("=" * (n*5))
        print("".join(map(str, dining_philosophers.status)), " : ",
              str(dining_philosophers.status.count('  E  ')))
        print("".join(map(str, dining_philosophers.chopstick_holders)))
        print("".join("{:3d}  ".format(m) for m in dining_philosophers.meals), " : ",
              str(sum(dining_philosophers.meals)))
        time.sleep(0.1)
    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    main()