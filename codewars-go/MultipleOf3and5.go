package main

import "fmt"

func Multiple3And5(number int) int {
	sum := 0

	for i := 1; i < number; i++ {
		if i%3 == 0 {
			fmt.Println(i)
			sum += i
			continue
		}
		if i%5 == 0 {
			fmt.Println(i)
			sum += i
			continue
		}
	}

	fmt.Println("The sum of all the multiples of 3 or 5 below ",number," is", sum)
	return sum
}

func main() {
Multiple3And5(10)
}
