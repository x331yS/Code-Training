package main


// Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.


func BoolToWord(word bool) string {
	if word {
		return"Yes"
	}
		return"No"
}

func main() {
	BoolToWord(true)
}

// Time to finish : 1 min 28 sec