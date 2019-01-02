#ifndef candpy_h__
#define candpy_h__

//Scalar args...
extern int addTwoInts(int a, int  b);
extern float addTwoFloats(float a, float b);


//Let's try using a struct.
typedef struct {
    float a,b;
} twoFloatsStruct;

extern float addTwoFloatsByStruct(twoFloatsStruct twoFloats);

#endif