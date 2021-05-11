package main

func Maps(x []int) {
	i := 0
	for i = 0; i < len(x); i++ {
		x[i] = x[i]*2
		print(x[i])
	}
}
func main() {
	Maps([]int{4, 2, 3})
}
