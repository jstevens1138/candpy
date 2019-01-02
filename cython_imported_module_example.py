import cython_so_example

print "Running through our library functions..."

print "Adding ints 1 and 2"
result_ints = cython_so_example.addTwoInts(1, 2)
print result_ints

print "Adding floats 3.5 and 3.4:"
result_floats = cython_so_example.addTwoFloats(3.5, 3.4)
print result_floats

print "Adding floats 5.6 and 2.2 by means of struct"
result_struct = cython_so_example.addTwoFloatsByStruct({'a': 5.6, 'b': 2.2})
print result_struct
