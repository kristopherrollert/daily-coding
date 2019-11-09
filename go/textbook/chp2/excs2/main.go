package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"

	"../excs2/distconv"
	"../excs2/massconv"
	"../excs2/tempconv"
)

func main() {
	if len(os.Args) > 1 {
		for _, arg := range os.Args[1:] {
			t, err := strconv.ParseFloat(arg, 64)
			if err != nil {
				fmt.Fprintf(os.Stderr, "conv: %v\n", err)
				os.Exit(1)
			}
			convertAndPrint(t)
		}
	} else {
		reader := bufio.NewReader(os.Stdin)
		fmt.Print("Enter value to convert: ")
		text, err := reader.ReadString('\n')
		if err != nil {
			fmt.Fprintf(os.Stderr, "conv: %v\n", err)
			os.Exit(1)
		}

		t, err := strconv.ParseFloat(text, 64)
		if err != nil {
			fmt.Fprintf(os.Stderr, "conv: %v\n", err)
			os.Exit(1)
		}
		convertAndPrint(t)
	}
}

func convertAndPrint(num float64) {
	f := tempconv.Fahrenheit(num)
	c := tempconv.Celsius(num)
	fmt.Printf("%s = %s, %s = %s\n",
		f, tempconv.FToC(f), c, tempconv.CToF(c))

	ft := distconv.Feet(num)
	m := distconv.Meters(num)
	fmt.Printf("%s = %s, %s = %s\n",
		ft, distconv.FToM(ft), m, distconv.MToF(m))

	p := massconv.Pounds(num)
	kg := massconv.Kilograms(num)
	fmt.Printf("%s = %s, %s = %s\n",
		p, massconv.PToKg(p), kg, massconv.KgToP(kg))

}
