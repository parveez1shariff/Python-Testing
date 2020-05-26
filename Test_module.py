# To check module import sys
# sys.builtin_module_names

import time

while True:
    with open("Vegetable.txt") as myfile:
        content = myfile.read()
    time.sleep(10)
    print(content)
