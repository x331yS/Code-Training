package main

import (
	"strings"
)

func RepeatStr(repetitions int, value string) string {
	return strings.Repeat(value, repetitions)
}

func main () {
	RepeatStr(4, "a")
}