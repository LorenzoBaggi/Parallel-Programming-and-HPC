import random
import time
from numba import jit
# jit (just in time compiler) transforms python code into C code
# we should specify the atomic parts of the code
# where atomic parts means that we can not divide anymore
# in this code, let's find the atomic parts

class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindPi:
    def __init__(self):
        self.n = 0
        self.i = 0

    # static method does not have access to elements inside the class
    def throw_points(self, nn):
        (self.i, self.n) = self.throw_points_static(nn)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def throw_points_static(nn):
        i = 0
        n = 0
        for _ in range(nn):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            r = x**2 + y**2
            n += 1
            if r <= 1:
                i += 1
        return i, n

    def value_of_pi(self):
        return 4 * self.i / self.n