package main


//Messi is a soccer player with goals in three leagues:
//
//LaLiga
//Copa del Rey
//Champions
//Complete the function to return his total number of goals in all three leagues.
//
//Note: the input will always be valid.


func main() {
Goals(5, 8 , 12)
}


func Goals(laLigaGoals, copaDelReyGoals, championsLeagueGoals int) int {
	return laLigaGoals + copaDelReyGoals + championsLeagueGoals
}

// Time to finish : 48 sec