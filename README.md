# Parallel-Programming-and-HPC
Python files created following the course on the following link: https://www.youtube.com/watch?v=3tl2YEYbaKk&amp;list=PL30NBs02RsiUbmXVPDo56APsU0xa6gfL2

First three lectures involve the problem of PI estimation, which takes too long to run on python.

- First lecture shows the code to do this calculation, also creating some classes.
- Second lecture then elaborates on this problem and addresses it with the help of multi-threading. This lecture shows that having multi-threads do not help the situation, indeed, there is the so called problem of GIL, Global Interpreter Lock.
So, one thread runs and the others sleep, sequentially. this problem is solved with the help of NUMBA and JIL (just in time compiler)
- Third lecture shows how to implement the PI estimation using mutiple threads in parallel, obtaning a high efficiency very fast
- Fourth lecture starts showing the problem of race condition, which, generates when multiple threads run in parallel. Then it is introduced the problem of deadlocks, with the example of two banks account and an infinite loop. This problem is also tackeld in the next lecture, with the famous dining philosophers problem.
- Fifth lecture here we dealt w/ the problem of dining philosophers, solving it into two different ways. Firstly, using Lock class, and then, Semaphore one.
- Sixth lecture
