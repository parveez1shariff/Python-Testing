# This code is to test pandas

import time
import os
import pandas

while True:
    if os.path.exists("original.csv"):
        data = pandas.read_csv("original.csv")
        print(data.mean())
    else:
        print("File does not exist")
    time.sleep(10)