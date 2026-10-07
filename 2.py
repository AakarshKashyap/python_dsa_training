import threading
import time
sema = threading.Semaphore(3)
def accessing():
    print(threading.current_thread().name, "waiting")
    sema.acquire()
    print(threading.current_thread().name,"accessing")