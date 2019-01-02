from ctypes import *

candpy = CDLL("candpy.so")

# Ints work easily.
print "About to add 1 and 3."

intsResult = candpy.addTwoInts(1, 2)
# Should be 3.
print intsResult

# What about floats?
print "Attempting to add two floats, 3.2 and 3.2."
try:
    floatsResult = candpy.addTwoFloats(3.2, 3.2)
except Exception as e:
    # Hmmmmmm...
    print e

# Yeah, that didn't work.

# From the ctypes documentation, "None, integers, bytes objects and (unicode) strings are the only native Python
# objects that can directly be used as parameters..." and with this in mind, we know to use the conversion functions
# available to us for the specific type(s) we're dealing with.
print "Adding two floats, 3.2 and 3.2, with the two args wrapped in c_float."
floatsResultBetter = candpy.addTwoFloats(c_float(3.2), c_float(3.2))
print floatsResultBetter

# It still seems to be wrong! That's because we must set the method's restype.
candpy.addTwoFloats.restype = c_float

# Now we're golden.
print "Adding the two floats with the args wrapped with and the function restype set as c_float."
floatsResultBest = candpy.addTwoFloats(c_float(3.2), c_float(3.2))
print floatsResultBest

print "All done!"