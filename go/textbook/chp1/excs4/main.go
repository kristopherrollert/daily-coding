// Exercise 1.4: Modify dup2 to print the names of all files in which each
// duplicated line occurs.
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	files := os.Args[1:]
	if len(files) == 0 {
		counts := make(map[string]int)
		countLinesStdin(counts)
		for line, n := range counts {
			if n > 1 {
				fmt.Printf("%d\t%s\n", n, line)
			}
		}
	} else {
		counts := make(map[string][]string)
		for _, arg := range files {
			f, err := os.Open(arg)
			if err != nil {
				fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
				continue
			}
			countLines(f, counts)
			f.Close()
		}

		for line, fileList := range counts {
			if len(fileList) > 1 {
				printed := make(map[string]bool)
				for _, fileName := range fileList {
					if !printed[fileName] {
						fmt.Printf("%s ", fileName)
						printed[fileName] = true
					}
				}
				fmt.Printf(": %s\n", line)
			}
		}
	}
}

func countLinesStdin(counts map[string]int) {
	input := bufio.NewScanner(os.Stdin)
	for input.Scan() {
		counts[input.Text()]++
	}
}

func countLines(f *os.File, counts map[string][]string) {
	input := bufio.NewScanner(f)
	for input.Scan() {
		counts[input.Text()] = append(counts[input.Text()], f.Name())
	}
}
