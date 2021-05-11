package main

import (
	"strings"
)

//Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
//
//Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
//
//Create a function which translates a given DNA string into RNA.

func main() {
	DNAtoRNA("GCAT")
}

func DNAtoRNA(dna string) string {

	dna = strings.Replace(dna, "T", "U", -1)
	print(dna)
	return dna
}

// Time to finish : 4 min 06 sec