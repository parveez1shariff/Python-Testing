# This code is import other python modules
# import sys
# sys.prefix

import time
import os

while True: 
    if os.path.exists("Vegetable.txt"):
        with open("Vegetable.txt") as myfile:
            print(myfile.read())
    else:
        print("File does not exist")
    time.sleep(10)