# Parallel-Programming-and-HPC
Python files created following the course on the following link: https://www.youtube.com/watch?v=3tl2YEYbaKk&amp;list=PL30NBs02RsiUbmXVPDo56APsU0xa6gfL2

First three lectures involve the problem of PI estimation, which takes too long to run on python (first lecture shows the code to do this calculation)
second lecture then elaborates on this problem and addresses it with the help of multi-threading
this lecture shows that having multi-threads do not help the situation, indeed, there is the so called problem of GIL, Global Interpreter Lock.
So, one thread runs and the others sleep, sequentially. this problem is solved with the help of NUMBA and JIL (just in time compiler)
