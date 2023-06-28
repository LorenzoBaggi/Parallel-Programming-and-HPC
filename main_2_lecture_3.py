from threading import Thread
from bc_numba import TicToc, FindPi
import time
import os

# main difference here: using NUMBA and JIT

if __name__ == "__main__":
    print("Running directly")
    tt = TicToc()
    tt.tic()
    n = 30_000_000
    find_pis = []     # multiple instances of class find_pi
    threads = []      # multiple instances of class threads

    for i in range(os.cpu_count()):
        find_pis.append(FindPi())
        threads.append(Thread(target=find_pis[i].throw_points, args=(n,)))
        print("Started thread number %d" %i)
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

print("PI = %.8f | N = %d / %d | TIME = %.5f" % (pi, inner, total, tt.toc()))
