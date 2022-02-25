from concurrent.futures import thread
import time
import threading
import sys
import os

sys.stderr.write("spam\n")

def getInput():
    global rand_num
    user_input = input('Enter Your Characters')
    print(rand_num)

def count():
    global rand_num
    while True:
        rand_num += time.time_ns()
        time.sleep(1)

rand_num = 0
thread1 = threading.Thread(target=getInput)
thread2 = threading.Thread(target=count)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(rand_num)

'''
def a():
    print("Function a is running at time: " + str(int(time.time())) + " seconds.")

def b():
    print("Function b is running at time: " + str(int(time.time())) + " seconds.")

threading.Thread(target=a).start()
threading.Thread(target=b).start()
'''