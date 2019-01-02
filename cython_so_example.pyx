cdef extern from "candpy.h":
    cpdef int addTwoInts(int a, int  b)
    cpdef float addTwoFloats(float a, float  b)
    ctypedef struct twoFloatsStruct:
        float a
        float b
    cpdef float addTwoFloatsByStruct(twoFloatsStruct twoFloats)

