# This is the basic version on how to calculate PI through MC methods, based on the
# ratio of two areas, one of a square and one of a circle of radius 1
# From this now on we can only improve in the next lectures

import random
import time

MAX_ITER = 10_000_000
count = 0
start_time = time.time()

for _ in range(MAX_ITER):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if (x ** 2 + y ** 2) < 1:
        count += 1

pi = 4 * count / MAX_ITER
end_time = time.time()
print("Pi value is: {:.5f}".format(pi))
print("It took this amount of time [s]: {:.5f}".format(end_time - start_time))