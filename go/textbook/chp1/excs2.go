// Exercise 1.2: Moidify the echo program to print the index and value of each
// of its arguments, one per line.
package main

import (
    "os"
    "fmt"
)

func main() {
    for i, arg := range os.Args {
        fmt.Println(i, arg)
    }
}
