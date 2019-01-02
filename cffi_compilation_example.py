# Inspired by Content from https://cffi.readthedocs.io/en/latest/overview.html

from cffi import FFI
ffibuilder = FFI()

# We could just read a header file here.
ffibuilder.cdef("""
    int addTwoInts(int a, int  b);
    float addTwoFloats(float a, float b);
    typedef struct {
        float a,b;
        ...;
    } twoFloatsStruct;
    float addTwoFloatsByStruct(twoFloatsStruct twoFloats);
""")

ffibuilder.set_source("_candpy_cffi",
                      """
                          #include "candpy.h"
                      """,
                      libraries=["candpy"])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)