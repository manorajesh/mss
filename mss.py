import time
import threading
import random
import sys
import base64

################################################# Initialization #######################################################

def init():
    print('''███╗   ███╗███████╗███████╗
████╗ ████║██╔════╝██╔════╝
██╔████╔██║███████╗███████╗
██║╚██╔╝██║╚════██║╚════██║
██║ ╚═╝ ██║███████║███████║
╚═╝     ╚═╝╚══════╝╚══════╝''')

    print("Mano's Secret Sharing")
    print("\nWelcome to MSS!\nNow, you can share secrets with your friends\nwith the help of a little Python script!\n")
    print("---\nJust smack at your keyboard, press enter, and watch the magic happen!\n")

def count():
    global rand_num
    while True:
        rand_num += int(time.time_ns()) # Source of entropy for random number (Possibly can be recreated; however, requires lots of knowledge about system)
        if stop_thread:
            break
        time.sleep(0.0001)

def sum(num_list):
    sum = 0
    for i in range(len(num_list)):
        sum += num_list[i]
    return sum

def randomParts(random_num, num_parts):
    og_rand = random_num
    while num_parts>1:
        x = random.randint(0, random_num) if random_num != 1 else 1
        yield x
        random_num -= x
        num_parts -= 1
    yield og_rand-x

rand_num = 0
numberOfParts = 0
part_list = []
rand_part_list = []
stop_thread = False

init()

################################################# User Input ###########################################################

try:
    while True:
        usr_input = input("How many parts should the password be in?\n> ")
        if usr_input.isdigit():
            if int(usr_input) < 10000000000000000:
                numberOfParts = int(usr_input)
                break
            else:
                print("\nThat's a lot of friends; more than the population of the Earth")
                print("Pick the important ones\n")
        else:
            print("\nPlease enter a number!")

    thread1 = threading.Thread(target=count)
    thread1.start()
    usr_input = input("\nEnter Random Characters\n> ")
    stop_thread = True
except KeyboardInterrupt:
    print("\n\nBye!\n")
    stop_thread = True
    sys.exit()

################################################# Part Gen #############################################################

rand_num = random.randint(random.randint(0, rand_num), rand_num) # Stops the password from being brute forced if somebody knew the time when the password was generated

while True:
    try:
        usr_input = input("\nWhat data type for password?\ninteger (i)\nfloat (f)\n")
    except KeyboardInterrupt:
        print("\n\nGracefully exit...\n")
        sys.exit()

    if usr_input == 'f':
        for i in range(numberOfParts):
            rand_part_list.append(random.random())
        for c in range(numberOfParts):
            part_list.append(rand_part_list[c] / sum(rand_part_list) * rand_num)
        break

    elif usr_input == 'i':
        part_list = list(randomParts(rand_num, numberOfParts))
        break

    else:
        print("\nPlease enter a valid option!\n")

################################################# Output ###############################################################

try:
    usr_input = input("\nWarning: The password is not encrypted and will display along with the parts!\nContinue? (Y/n)\n")
except KeyboardInterrupt:
    print("\n\nBye!\n")
    sys.exit()

if usr_input == "n":
    while True:
        usr_input = input("\nHow should the output be displayed?\nNot at all? (n)\nOnly the parts? (p)\nEverything? (e)\n> ")
        if usr_input == "n":
            print("\nCome Back Again!\n")
            sys.exit()
        elif usr_input == "p":
            print("\nThe Parts are: ")
            print(part_list)
            sys.exit()
        elif usr_input == "e":
            print("Parts: " + str(part_list))
            print("Password: " + str(sum(part_list)))
            sys.exit()
        else:
            print("\nPlease enter a valid option!\n")

print("\nParts: " + str(part_list))
print("Password: " + str(sum(part_list)))

### Base64 Encoding ###
print("\n---")
print("Parts in B64:")
for i in range(len(part_list)):
    print((base64.b64encode(bytes(str(part_list[i]), 'ascii'))).decode('ascii'))
print("\nPassword in B64: %s" % (base64.b64encode(bytes(str(rand_num), 'ascii'))).decode('ascii'))