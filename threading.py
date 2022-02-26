from concurrent.futures import thread
from email.mime import base
import time
import threading
import base64
from random import randint
import sys
import numpy

def count():
    global rand_num
    while True:
        rand_num += time.time_ns()
        time.sleep(0.5)

def randomParts(rand_num, numberOfParts, part_list):
    if numberOfParts < 2:
        print("Please select 2 or more parts to divide")
        sys.exit()

    part_list.append(randint(0, rand_num))
    part_list.append(rand_num-part_list[0])


rand_num = 0
numberOfParts = 2
parts_list = []

thread1 = threading.Thread(target=count)
thread1.start()

try:
    usr_input = input("Enter Random Characters: ")

except KeyboardInterrupt:
    thread1.join()
print(rand_num)

randomParts(100, 3, parts_list)
print(parts_list)

print(parts_list[0].to_bytes(10, 'big'))