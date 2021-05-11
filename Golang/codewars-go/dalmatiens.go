package main

//Your friend has been out shopping for puppies (what a time to be alive!)... He arrives back with multiple dogs, and you simply do not know how to respond!
//
//By repairing the function provided, you will find out exactly how you should respond, depending on the number of dogs he has.
//
//The number of dogs will always be a number and there will always be at least 1 dog.

func HowManyDalmatians(number int) string{
	var dogs = [4]string{"Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIENS!!!"}

	s := ""
	switch {
	case number <= 10 && number >= 1 :
		s = dogs[0]
	case number > 10 && number < 51 :
		s = dogs[1]
	case number == 101 :
		s = dogs[3]
	default :
		s = dogs[2]
	}
	print(s)
	return(s)


}

func main() {
	HowManyDalmatians(10)
	HowManyDalmatians(50)
	HowManyDalmatians(52)
	HowManyDalmatians(100)
	HowManyDalmatians(101)
}

// Time to finish : 22 min 40 sec