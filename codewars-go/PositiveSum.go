package main

func main() {
	PositiveSum([]int{1, 2, 3, 4, 5})
	PositiveSum([]int{1, -2, 3, 4, 5})
	PositiveSum([]int{-1, -2, -3, -4, -5})
}

func PositiveSum(numbers []int) int {
	var result int
	for _, x := range numbers {
		if x > 0 {
			result += x
		}
	}
	println(result)
	return result
}
