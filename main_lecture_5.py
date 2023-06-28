# The famous dining philosophers problem
# there are 5 philosophers at a table, with 5 chopstick
# 5 plates and 5 meals, one for each philosopher
# a philosopher can be in two separate states (think / eat)
# at the beginning, they are all thinking. then, one philosopher decides to eat
# to be able to eat, each philosopher must hold two chopsticks
# but if another philosopher decides to eat At that moment, there is a problem
# they will be in a position where all of them are waiting for another chopstick and this
# situation is called deadlock

import random
import time
from threading import Lock, Thread


# meals will be considered as jobs to be completed and philosophers as processes
# while chopsticks as resources (locks). each chopstick can be used by one philosopher

class DiningPhilosophers:
    def __init__(self, number_of_philosophers=5, meal_size=7):
        """[7 7 7 7 7]"""
        self.meals = [meal_size for _ in range(number_of_philosophers)]
        self.chopsticks = [Lock() for _ in range(number_of_philosophers)]
        self.status = ['  T  ' for _ in range(number_of_philosophers)]
        self.chopstick_holders = ['     ' for _ in range(number_of_philosophers)]

    def philosopher(self, i):
        j = (i + 1) % 5
        while self.meals[i] > 0:
            self.status[i] = '  T  '
            time.sleep(random.random())
            self.status[i] = '  _  '
            if not self.chopsticks[i].locked():
                self.chopsticks[i].acquire()
                self.chopstick_holders[i] = ' /  '
                time.sleep(random.random())
                if not self.chopsticks[j].locked():
                    self.chopsticks[j].acquire()
                    self.chopstick_holders[i] = ' /\  '
                    self.status[i] = '  E  '
                    time.sleep(random.random())
                    self.meals[i] -= 1
                    self.chopsticks[i].release()
                    self.chopstick_holders[i] = ' /  '
                    self.chopsticks[j].release()
                    self.chopstick_holders[i] = '    '
                    self.status[i] = '  T  '
                else:
                    self.chopsticks[i].release()
                    self.chopstick_holders[i] = '    '


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
