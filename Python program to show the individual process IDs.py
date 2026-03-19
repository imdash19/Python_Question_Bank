# In multiprocessing, processes are spawned by creating a Process object. Write a Python program to show the individual process IDs (parent process, process ID etc.) involved.
# Sample Output:
# Main line
# module name: __main__
# parent process: 23967
# process id: 27986
# function f
# module name: __main__
# parent process: 27986
# process id: 27987
# hello bob

import multiprocessing
import os

def f(name):
    print("function f")
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())
    print("hello", name)

if __name__ == "__main__":
    print("Main line")
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())

    p = multiprocessing.Process(target=f, args=("bob",))
    p.start()
    p.join()