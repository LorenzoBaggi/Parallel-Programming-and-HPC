import random
from threading import Thread
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
        for i in range(self.n):
            x = random.uniform(x_lower, x_upper)
            y = random.uniform(y_lower, y_upper)
            if (x ** 2 + y ** 2) <= 1:
                self.i += 1

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
