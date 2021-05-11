package main

//Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
//
//If the tail is right return true, else return false.
//
//The arguments will always be strings, and normal letters.
//
//For Haskell, body has the type of String and tail has the type of Char. For Go, body has type string and tail has type rune.

func CorrectTail(body string, tail rune) bool {
	if rune(Reverse(body)[0]) != tail {
		print(false)
		return false
	}
	return true
}

func Reverse(body string) string {
	runes := []rune(body)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func Reversed(body string) (result string) {
for _,v := range body {
result = string(v) + result
}
return
}

func main() {
	CorrectTail("fox", 'x')
}

// Time to finish : 6 min 22 sec

