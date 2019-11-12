package popcount

// pc[i] is the population count of i.
var pc [256]byte

func init() {
	for i := range pc {
		pc[i] = pc[i/2] + byte(i&1)
	}
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

func PopCountSingleBit(x uint64) int {
	var j byte = 1
	total := 0
	x_byte := byte(x)
	for i := 0; i < 64; i++ {
		if x_byte&j != 0 {
			total++
		}
		j *= 2
	}
	return total
}

func PopCountRemoveBit(x uint64) int {
	x_byte := byte(x)
	total := 0
	for x_byte != 0 {
		total++
		x_byte = x_byte & (x_byte - 1)
	}
	return total
}
