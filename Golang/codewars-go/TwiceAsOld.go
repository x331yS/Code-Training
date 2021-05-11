package main


func TwiceAsOld(dadYearsOld, sonYearsOld int) int {
	result := 1
	for dadYearsOld / 2 != sonYearsOld {
		dadYearsOld++
		sonYearsOld++
		result++
	}
	print(result)
	return result
}

func main () {
	TwiceAsOld(36,7)
}