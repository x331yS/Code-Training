package main

import (
	"unicode"
)

//Create a method IsUpperCase to see whether the string is ALL CAPS. For example:
//
//Exemple :
//type MyString string
//MyString("c").IsUpperCase() == false
//MyString("C").IsUpperCase() == true
//MyString("hello I AM DONALD").IsUpperCase() == false
//MyString("HELLO I AM DONALD").IsUpperCase() == true
//MyString("ACSKLDFJSgSKLDFJSKLDFJ").IsUpperCase() == false
//MyString("ACSKLDFJSGSKLDFJSKLDFJ").IsUpperCase() == true

func IsUpper(s string) bool {
	for _, r := range s {
		if !unicode.IsUpper(r) && unicode.IsLetter(r) {
			return false
		}
	}
	print(true)
	return true
}


func main (){
	IsUpper("HeLLO")
}

// Time to finish : 5 min 59 sec
