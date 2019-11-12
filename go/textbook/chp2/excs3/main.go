// Exercise 2.3: Rewrite PopCount to use a loop instead of a single expression.
// Compare the performance of the two versions.
package main

import (
	"fmt"
	"time"
)

// pc[i] is the population count of i.
var pc [256]byte

func init() {
	for i := range pc {
		pc[i] = pc[i/2] + byte(i&1)
	}
}

func main() {
	var start time.Time
	var totalLoop time.Duration
	var totalNormal time.Duration
	for i := 1; i < 1000000; i++ {
		start = time.Now()
		PopCountNormal(100)
		totalNormal += time.Since(start)
	}

	for j := 1; j < 1000000; j++ {
		start = time.Now()
		PopCountLoop(100)
		totalLoop += time.Since(start)
	}

	fmt.Printf("Normal runtime (for 1 million runs): %q\n", totalNormal)
	fmt.Printf("Loop runtime (for 1 million runs): %q\n", totalLoop)

}

// PopCount returns the population count (number of set bits) of x.
func PopCountLoop(x uint64) int {
	var total byte
	var i uint64
	for i = 1; i < 8; i++ {
		total += pc[byte(x>>(i*8))]
	}
	return int(total)
}

func PopCountNormal(x uint64) int {
	return int(pc[byte(x>>(0*8))] +
		pc[byte(x>>(1*8))] +
		pc[byte(x>>(2*8))] +
		pc[byte(x>>(3*8))] +
		pc[byte(x>>(4*8))] +
		pc[byte(x>>(5*8))] +
		pc[byte(x>>(6*8))] +
		pc[byte(x>>(7*8))])
}
