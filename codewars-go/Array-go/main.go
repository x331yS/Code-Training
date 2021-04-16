package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Println("incomplete")
		return
	}
	var argsOne = os.Args[1]
	var argsTwo = os.Args[2]
	var nbrcolonne, _ = strconv.Atoi(argsOne)
	var nbrligne, _ = strconv.Atoi(argsTwo)

	if valueValid(argsOne) == false || valueValid(argsTwo) == false {
		fmt.Println("It's not an int")
		return
	}
	if nbrligne == 0 || nbrcolonne == 0 {
		fmt.Println("not possible")
		return
	}
	showxLine(nbrcolonne)
	if nbrligne > 2 {
		shownumberLine(nbrcolonne, nbrligne)
	}
	if nbrligne > 1 {
		showxLine(nbrcolonne)
	}
}

func showxLine(longueur int) {
	fmt.Print("X")
	for i := 0; i < longueur-2; i++ { // sinon il va croire le nb de tiret = nb colonne
		fmt.Print("-")
	}
	if longueur > 1 {
		fmt.Print("X")
	}
	fmt.Print("\n")
}

func shownumberLine(longueur int, hauteur int) {
	for i := 0; i < hauteur-2; i++ {
		fmt.Print(i % 10)
		for j := 0; j < longueur-2; j++ {
			fmt.Print(" ")
		}
		if longueur > 1 {
			fmt.Print((hauteur - 2 + i) % 10)
		}
		fmt.Print("\n")
	}
}

func valueValid(value string) bool {

	for _, v := range value {

		if v < 48 || v > 57 {
			return false
		}

		return true
	}
	return true
}
