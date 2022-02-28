from concurrent.futures import thread
from email.mime import base
import time
import threading
import base64
import numpy as np, numpy.random

def count():
    global rand_num
    while True:
        rand_num += time.time_ns()
        if stop_thread:
            break
        time.sleep(0.5)

rand_num = 0
numberOfParts = 6
part_list = []
rand_part_list = []
stop_thread = False

thread1 = threading.Thread(target=count)
thread1.start()

usr_input = input("Enter Random Characters: ")
stop_thread = True
print(rand_num)

for i in range(numberOfParts):
    rand_part_list.append(np.random.random())

for c in range(numberOfParts):
    part_list.append(rand_part_list[c] / numpy.sum(rand_part_list) * rand_num)

print(part_list)
print(f"{numpy.sum(part_list):1f}")

print(part_list[0].to_bytes(10, 'big'))