// Exercise 2.3: Rewrite PopCount to use a loop instead of a single expression.
// Compare the performance of the two versions.
package popcount

// pc[i] is the population count of i.
var pc [256]byte

func init() {
	for i := range pc {
		pc[i] = pc[i/2] + byte(i&1)
	}
}

// PopCount returns the population count (number of set bits) of x.
func PopCount(x uint64) int {
	var total byte
	var i uint64
	for i = 1; i < 8; i++ {
		total += pc[byte(x>>(i*8))]
	}
	return int(total)
}
