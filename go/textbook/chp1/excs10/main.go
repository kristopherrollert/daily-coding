// Exercise 1.10: Find a web site that produces a large amount of data.
// Investigate caching by running fetchall twice in succession to see whether
// the reported time changes much. Do you get the same content each time? Modify
// fetchall to print its output to a file so it can be examined.

// My Response:
// My function writes to a file with the url plus the index which it was passed.
// When I did a statically delivered page the results were identical, but when
// I did a more dynamic page, like google, the results varried a lot. I used
// the unix command diff to compare.

package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	start := time.Now()
	ch := make(chan string)
	for i, url := range os.Args[1:] {
		go fetch(url, i, ch) // start a goroutine
	}
	for range os.Args[1:] {
		fmt.Println(<-ch) // receive from channel ch
	}
	fmt.Printf("%.2fs elapsed\n", time.Since(start).Seconds())
}

func fetch(url string, num int, ch chan<- string) {
	start := time.Now()
	resp, err := http.Get(url)
	if err != nil {
		ch <- fmt.Sprint(err) // send to channel ch
		return
	}

	name := strings.Split(url, ".")[0]
	name = strings.TrimPrefix(name, "http://")
	name = strings.TrimPrefix(name, "https://")

	file, err := os.OpenFile(name+strconv.Itoa(num)+".txt", os.O_RDWR|os.O_CREATE, 755)
	if err != nil {
		ch <- fmt.Sprintf("while creating/opening file %s: %v", url, err)
		return
	}

	nbytes, err := io.Copy(file, resp.Body)
	resp.Body.Close() // don't leak resources
	if err != nil {
		ch <- fmt.Sprintf("while reading %s: %v", url, err)
		return
	}
	secs := time.Since(start).Seconds()
	ch <- fmt.Sprintf("%.2fs  %7d  %s", secs, nbytes, url)
}
