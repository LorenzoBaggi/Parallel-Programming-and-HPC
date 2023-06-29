# PI ESTIMATION with only 4 threads, each thread should use different quadrant
# the program should not cause race condition, deadlock and GIL
# thread 0, thread 1, thread 2, thread 3
# thread 0 will use Q1, thread1 Q2, ...
# for each quadrant, there is a range for (x, y)
# for example, quadrant 1 will have x > 0, x < 1 and y > 0 and y < 1
# quadrant 2 will have -1 < x < 0 and 0 < y < 1 and so on

import random
from threading import Thread
from numba import jit
import time


class MontecarloPi:
    def __init__(self, n, limits):
        self.n = n
        self.i = 0
        self.limits = limits

    def throw_points(self):
        x_lower = self.limits[0][0]
        x_upper = self.limits[0][1]
        y_lower = self.limits[1][0]
        y_upper = self.limits[1][1]
        self.i = self.throw_points_static(self.n, x_lower, x_upper, y_lower, y_upper)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def throw_points_static(n, x_lower, x_upper, y_lower, y_upper):
        i = 0
        for _ in range(n):
            x = random.uniform(x_lower, x_upper)
            y = random.uniform(y_lower, y_upper)
            if (x ** 2 + y ** 2) <= 1:
                i += 1
        return i


if __name__ == "__main__":
    quadrants = [
        [[0, 1], [0, 1]],
        [[-1, 0], [0, 1]],
        [[-1, 0], [-1, 0]],
        [[0, 1], [-1, 0]]
    ]
    start_time = time.time()
    find_pis = [MontecarloPi(1_000_000, quadrants[i]) for i in range(4)]
    threads = [Thread(target=find_pis[i].throw_points()) for i in range(4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    inner = 0
    total = 0
    for find_pi in find_pis:
        inner += find_pi.i
        total += find_pi.n
    pi = 4 * inner / total
    end_time = time.time()
    print(f"Points: {inner}/{total}")
    print(f"Estimated Pi: {pi:.6f}")
    print(f"Required time: {(end_time - start_time):.3f}")
