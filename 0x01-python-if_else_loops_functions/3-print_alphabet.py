#!/usr/bin/python3

for x in range(97, 123):
    a = chr(x)
    if a != 'q' and a != 'e':
        print("{}".format(a), end="")
