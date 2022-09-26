package main

//import is required to do most things in go
//fmt allows for input and output like println, input, etc
//strings allow for editing of strings, as shown in colormixer()
import (
	"fmt"
	"strings"
)

//main function for calling all of my programs
func main() {

	//setting variable so go can listen for input
	var function string
	fmt.Print("Enter a function to call: ")
	fmt.Scan(&function)

	//if statement where i put all my functions
	//later may be replaced if i find a better way to run
	//functions like in python
	if function == "day_converter" {
		day_converter()
	} else if function == "roman_numerals" {
		roman_numerals()
	} else if function == "colormixer" {
		colormixer()
	} else { //error catching
		fmt.Println("This function has not been created yet.")
		fmt.Println()
		main()
	}
}

func day_converter() {
	// this program takes no arguments
	// asks user for input of a number 1-7
	// prints day of the week corresponding to the num
	// uses println because yes

	//creating variable
	//var i int
	//this var creation format looks kinda weird
	i := 0
	fmt.Print("Type a number from 1-7: ")
	//listening for input
	fmt.Scan(&i)

	//if statement for days of the week
	if i == 1 {
		fmt.Println("Sunday")
	} else if i == 2 {
		fmt.Println("Monday")
	} else if i == 3 {
		fmt.Println("Tuesday")
	} else if i == 4 {
		fmt.Println("Wednesday")
	} else if i == 5 {
		fmt.Println("Thursday")
	} else if i == 6 {
		fmt.Println("Friday")
	} else if i == 7 {
		fmt.Println("Saturday")
	} else { //error catching
		fmt.Println("This number is out of range. Please try again.")
		fmt.Println()
		day_converter()
	}
}

func roman_numerals() {
	//function roman_numerals takes no arguments
	//asks user for an input between 1 and 10
	//gives them the roman numeral corresponding to the number
	//may be revamped with a loop instead of if statements

	//input var creation & listen
	var number int
	fmt.Print("Enter a number between 1 and 10:")
	fmt.Scan(&number)

	//if statement
	if number == 1 {
		fmt.Println("I")
	} else if number == 2 {
		fmt.Println("II")
	} else if number == 3 {
		fmt.Println("III")
	} else if number == 4 {
		fmt.Println("IV")
	} else if number == 5 {
		fmt.Println("V")
	} else if number == 6 {
		fmt.Println("VI")
	} else if number == 7 {
		fmt.Println("VII")
	} else if number == 8 {
		fmt.Println("VIII")
	} else if number == 9 {
		fmt.Println("IX")
	} else if number == 10 {
		fmt.Println("X")
	} else {
		fmt.Println("Your answer is invalid. Please try again.")
		fmt.Println()
		roman_numerals()
	}

}

func colormixer() {
	// func colormixer takes no arguments
	// it asks user for two color inputs to mix
	// mixes colors with string concatenation and if statements
	// prints output based on if statement

	//firstcolor variable input making
	fmt.Println("Enter a primary color (red, blue, yellow): ")
	var firstcolor string
	fmt.Scan(&firstcolor)

	//secondcolor variable input making
	fmt.Print("Enter another primary color (red, blue, yellow): ")
	var secondcolor string
	fmt.Scan(&secondcolor)

	//concatentation
	var combined string = strings.ToLower(firstcolor + secondcolor)


  //if statement setup
	if combined == "redblue" || combined == "bluered" {
		fmt.Print("When your colors mix, they become purple.")

	} else if combined == "redyellow" || combined == "yellowred" {
		fmt.Print("When you colors mix, they become orange.")

	} else if combined == "blueyellow" || combined == "yellowblue" {
		fmt.Print("When your colors mix, they become green.")

	} else {
		fmt.Print("Your input was rejected. Please try again.")
		fmt.Print()
		colormixer()
	}

}
