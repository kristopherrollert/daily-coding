// Exercise 1.3: Experiment to measure the difference in running time between
// our potentially inefficient versions and the one that uses strings.Join.
package main

import (
    "fmt"
    "time"
    "os"
    "strings"
)

func main() {
    var time1, time2, time3 time.Duration
    time1 = timeFunction(ex1)
    time2 = timeFunction(ex2)
    time3 = timeFunction(ex3)
    fmt.Println("---- Exercise 1:", time1)
    fmt.Println("---- Exercise 2:", time2)
    fmt.Println("---- Exercise 3:", time3)
}

func timeFunction(ex func()) time.Duration{
    var start time.Time
    var total time.Duration
    for i := 1; i < 100; i++ {
        start = time.Now()
        ex()
        total += time.Since(start)
    }
    return total / 100
}

func ex1()  {
    var s, sep string
    for i := 1; i < len(os.Args); i++ {
        s += sep + os.Args[i]
        sep = " "
    }
    fmt.Println(s)
}

func ex2() {
    s, sep := "", ""
    for _, arg := range os.Args[1:] {
        s += sep + arg
        sep = " "
    }
    fmt.Println(s)
}

func ex3() {
    fmt.Println(strings.Join(os.Args[1:], " "))
}
