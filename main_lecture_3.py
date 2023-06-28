from threading import Thread
from bc import TicToc, FindPi
import time
import os

if __name__ == "__main__":
    print("Running directly")
    tt = TicToc()
    tt.tic()
    n = 10_000_000
    find_pis = []     # multiple instances of class find_pi
    threads = []      # multiple instances of class threads

    # 12 threads on my machine. most of them when running, reports the status S (Sleeping), one of them
    # has the status R, running, and it changes position. They are running in a sequential mode
    # e.g., one is running, then, another is running, then another one is running and so on
    # this situation is called GIL, Global Interpreter Lock
    # it says that only one thread is running at a time
    # indeed, it took me 133 seconds w/ 10_000_000 as n to get 3.141566 (N = 120_000_000)
    # I'd like to run all the threads in parallel! So, I'd like to get rid of GIL
    # NUMBA will help me, it has Jit, just in time compiler.

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
