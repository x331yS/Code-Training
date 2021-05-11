package main

import (
	"strings"
)

func main() {
	RemoveChar("Wdtf")
	RemoveChar("Wddezdzeftf")
	RemoveChar("zaeaWadtfeazeaz")

}

func RemoveFirstChar(word string) string {
	t := strings.Trim(word, string(word[0]))
	println(t)
	return t
}

func RemoveLastChar(word string) string {
	y := word[len(word)-1:]
	t := strings.Trim(word, y)
	println(t)
	return t
}

func RemoveChar(word string) string {
	println(word[1:len(word)-1])
	return word[1:len(word)-1]
}
