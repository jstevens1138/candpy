from ctypes import *

candpy = CDLL("candpy.so")

class twoFloatsStruct(Structure):
    _fields_ = [("a", c_float),
                ("b", c_float)]

candpy.addTwoFloatsByStruct.restype = c_float

print "Using a struct, adding floats 3.5 and 2.0."
my_floats_struct = twoFloatsStruct(a=3.5, b=2.0)
result = candpy.addTwoFloatsByStruct(my_floats_struct)
print result

print "All done."