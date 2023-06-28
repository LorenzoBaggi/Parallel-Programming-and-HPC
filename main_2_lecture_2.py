from bc import TicToc, FindPi
from threading import Thread
import time

# Once the Thread is created, the start() method is called to start the execution of the throw_points()
# method in the new thread. This allows the main thread to continue with the loop and print the progress
# of the calculation of pi.

if __name__ == "__main__":
    print("Running directly")
    tt = TicToc()
    tt.tic()
    finding_pi = FindPi()
    n = 10_000_000
    # finding_pi.throw_points(10_000_000)
    Thread(target=finding_pi.throw_points, args=(n,)).start()

    for _ in range(25):
        pi = finding_pi.value_of_pi()
        print("PI = %.8f | N = %d / %d | TIME = %.5f" % (pi, finding_pi.i, finding_pi.n, tt.toc()))
        time.sleep(1)