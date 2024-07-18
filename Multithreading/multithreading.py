## Multithreading
# When to use ?
# I/O Bound Task: Tasks that spend more time waiting for I/O Operations (e.g, file operations, network request)
# Concurrent execution: When you want to improve the throughput of your application by 

import time
import threading

def print_numbers():
    for i in range(5):
        time.sleep(2);
        print(f"Numbers: {i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letters: {letter}")

# Create 2 thread
t1 = threading.Thread(target=print_numbers())
t2 = threading.Thread(target=print_letters())

t = time.time()
# start the thread
t1.start()
t2.start()

# Wait for the threads to complete
t1.join()
t2.join()

finished_time = time.time() - t
print(finished_time)