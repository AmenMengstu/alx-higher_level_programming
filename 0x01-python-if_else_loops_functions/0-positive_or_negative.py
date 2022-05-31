#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{%s} is positive".format(number))
elif number == 0:
    print("{%s} is zero".format(number))
else:
    print("{%s} is negative".format(number))
