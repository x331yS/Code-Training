package main

import (
	"strings"
)

//Write a function which converts the input string to uppercase.

func main() {
	MakeUpperCase("Hello world dude")

}

func MakeUpperCase(str string) string {
			s := strings.ToUpper(str)
	print(s)
	return s
}

// Time to finish : 7 min 32 sec
