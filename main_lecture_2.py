# Link of the lesson: https://www.youtube.com/watch?v=0WSRhvA8z8U&list=PL30NBs02RsiUbmXVPDo56APsU0xa6gfL2&index=2

import random
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

MAX_ITER = 5_000
count = 0
x = []
y = []
start_time = time.time()

for _ in range(MAX_ITER):
    x.append(random.uniform(-1, 1))
    y.append(random.uniform(-1, 1))

fig, ax = plt.subplots()
ax.add_patch(Rectangle((-1, -1), 2, 2, alpha=0.2, color="yellow"))
ax.add_patch(Circle((0, 0), 1, alpha=0.2, color="red"))
plt.scatter(x, y, s = 1, color="black")
plt.axhline(0, color="red")
plt.axvline(0, color="red")
plt.show()

