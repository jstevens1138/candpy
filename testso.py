from ctypes import *

lib = CDLL("libsotest.so")
x = lib.doSlowThing()
print x
