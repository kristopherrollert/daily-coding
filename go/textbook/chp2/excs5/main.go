// Exercise 2.5: The expression x&(x-1) clears the rightmost non-zero bit of x.
// Write a version of PopCount that counts bits by using this fact, and assess
// its performance.
package main

import (
	"fmt"
	"time"

	"../excs5/popcount"
)

func main() {
	var start time.Time
	var totalLoop time.Duration
	var totalNormal time.Duration
	var totalSingleBit time.Duration
	var totalRemoveBit time.Duration
	for i := 1; i < 1000000; i++ {
		start = time.Now()
		popcount.PopCountNormal(174467404370935115)
		totalNormal += time.Since(start)
	}

	for j := 1; j < 1000000; j++ {
		start = time.Now()
		popcount.PopCountLoop(174467404370935115)
		totalLoop += time.Since(start)
	}

	for k := 1; k < 1000000; k++ {
		start = time.Now()
		popcount.PopCountSingleBit(174467404370935115)
		totalSingleBit += time.Since(start)
	}

	for l := 1; l < 1000000; l++ {
		start = time.Now()
		popcount.PopCountRemoveBit(174467404370935115)
		totalRemoveBit += time.Since(start)
	}

	fmt.Printf("Normal runtime (for 1 million runs): %q\n", totalNormal)
	fmt.Printf("Loop runtime (for 1 million runs): %q\n", totalLoop)
	fmt.Printf("Single Bit runtime (for 1 million runs): %q\n", totalSingleBit)
	fmt.Printf("Remove Bit runtime (for 1 million runs): %q\n", totalRemoveBit)

}
