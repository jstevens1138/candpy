package main
import (
    "C"
)

//export doSlowThing
func doSlowThing() C.int {
    var sum C.int = 0
    for i := 0; i < 20000; i++ {
        for x := 0; x < 20000; x++ {
            sum++
        }
    }
    return sum
}

func main() {}
