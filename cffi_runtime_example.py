from _candpy_cffi import ffi, lib

print "Let's add the integers 1 and 3."
result = lib.addTwoInts(1, 3)
print result

print "Let's add the floats 1.3 and 3.3."
result = lib.addTwoFloats(1.3, 3.3)
print result

print "Let's try using a struct to add 2.333 and 5.5."
my_float_struct = ffi.new("twoFloatsStruct *",
                          {"a": 2.3333,
                           "b": 5.5}
                          )
result = lib.addTwoFloatsByStruct(my_float_struct[0])
print result