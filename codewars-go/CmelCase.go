package main

import "strings"

//Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
//
//Examples
//"the-stealth-warrior" gets converted to "theStealthWarrior"
//"The_Stealth_Warrior" gets converted to "TheStealthWarrior"



func ToCamelCase(s string) string {
	var v rune
	var output string
	var previous = '0'
	for _, v = range s {
		if previous == '-' || previous == '_' {
			if v >= 97 && v <= 122 {
				output += string(v-32)
			} else {
				output += string(v)
			}
		} else {
			if v != '-' && v != '_' {
				output += string(v)
			}
		}

		previous = v
	}
	print(output)
	return output
}


func main() {
	ToCamelCase("The_stealth_Warrior")
	print("\n")
	ToCamelCase("the-Stealth-Warrior")
	print("\n")
	ToCamelCase("left-Yellow-up-Green-Street-Yellow-desert")
	print("\n")
	ToCamelCase("down-side-desert-Wall-bridge-down-right")

}

// Time to finish : 32 min 8 sec


func CamelCase(s string) string {
	var v rune
	var previous = '0'
	for _, v = range s {

		if previous == '-' || previous == '_' {
			if v >= 97 && v <= 122 {
				s = strings.Replace(s, string(v), string(v-32), -1)
			}
		}

		previous = v
	}

	s = strings.Replace(s, "-", "", -1)
	s = strings.Replace(s, "_", "", -1)

	print(s)
	return s

}