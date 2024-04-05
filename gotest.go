package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Hello")

	go doSomthing()

	time.Sleep(4 * time.Millisecond)
}

func doSomthing() {
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}
}
