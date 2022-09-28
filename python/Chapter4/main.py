import turtle as t

def bug_collector():
    #program bug_collector receives no arguments
    #it prompts the user for how many bugs they collected throughout 5 days
    #then displays the total
    
    #entrance statement
    print("Welcome to Bug Masters bug collection system.")
    totalbugs = 0 #accumulator
   
   
    #for every day in new range 1-5, do these things
    for daycount in range(1,5+1):
    
        #seperated these so that i could show day count in input statement
        print("How many bugs did you collect on day",daycount,end='')
        bugcount = int(input("? "))
        
        #input validation for negative numbers
        while bugcount < 0 :
            print("Please enter a valid entry for the bug journal.\n")
            return
        totalbugs += bugcount
    
    #output
    print("Great job, you collected",totalbugs,"bugs this week. You're the bug master!")
    
    
def distance_traveled():
    #function distance_traveled receives no arguments
    #it prompts the user for a speed and amount of hours vehicle previously traveled
    #then outputs the amount of miles the car traveled in the amount of hours from 1-amount of hours traveled
    
    
    speed = int(input("Enter the speed of the vehicle in mph: "))
    
    #input validation
    while speed < 0 :
        print("Please enter a valid entry for speed.\n")
        return
        
    hours = int(input("Enter how many hours the vehicle traveled: "))
    
    #input validation
    while hours < 0 :
        print("Please enter a valid entry for your hours.\n")
        return
        
    #header for chart
    print("\nHour\tDistance Traveled")
    print("-----------------------")
    
    
    for travel in range(1,hours+1):
    #chart output every hour
        print(travel,"\t\t",speed*travel)
        
        
def pennies():
    #function pennies receives no arguments
    #it asks user how many days they want to double their pennies
    #then outputs that amount of days with the doubled pennies each day
    
    
    daycount = int(input("How many days do you want to acquire pennies? "))
    #input validation
    while daycount < 0 :
        print("Please enter a valid entry for the amount of days.\n")
        return
    
    #header for chart
    print("\nDay\tSalary")
    print("-------------")
    salary = 1 #accumulator, sorta
    for days in range(1,daycount):
        if days == 1:
            print(days,"\t$","0.01")
        salary = (salary * 2)
        print(days + 1,"\t$",format(salary / 100,'.2f'))
        
        
def hogwarts_tuition():
    #program hogwarts_tuition receives no arguments
    #tuition for hogwarts increases 3% every year
    #for this reason, a chart is provided to the user to show his tuition increase
    
    #constant, and accumulator sorta
    SEMESTER_TUITION = 8000
    
    #header for chart
    print("Year\tTuition Cost")
    print("--------------------")
    
    for year in range(1,5+1):
        SEMESTER_TUITION += (SEMESTER_TUITION * 0.03)
        print(year,"\t$",format(SEMESTER_TUITION*2, '.2f'))
        

def population():
    #function population receives no arguments
    #simulates population growth given a
    #starting # of organisms,
    #average daily increase %,
    #and number of days to simulate
    #outputs result in a chart style
    
    starting_pop = int(input("Enter the starting population: "))
    
    #input validation for starting_pop
    while starting_pop < 0 :
        print("Please enter a valid entry for the starting population.\n")
        return
    
    daily_growth = int(input("Enter the percent of daily growth: "))
    
    daycount = int(input("Enter the number of days to simulate: "))
    
    #input validation for daycount
    while daycount < 1 :
        print("Please enter a valid entry for the amount of days.\n")
        return
    
    #header for chart
    print("\nDay\tProjected Population")
    print("----------------------------")
    
    
    for days in range(1,daycount):
        starting_pop += starting_pop*(daily_growth/100)
        if days == 1:
            print(days,"\t\t","2")
        print(days+1,"\t\t",starting_pop)
        
        
def reverse_triangle():
    #program reverse_triangle receives no arguments.
    #generates an upside-down right triangle based on the size the user specifies
    
    size = int(input("Enter the base size of the triangle: "))
    for triangle in range(size, 0, -1):
        line = "*" * triangle
        print(line)
        
    
def stair_pattern2():
    #function stair_pattern2 receives no arguments
    #it prints a hollow stair pattern based on what the user specifies as the number of stairs
    
    stairs = int(input("Enter the number of stairs: "))
    while stairs < 1 :
        print("Please enter a valid entry for the amount of stairs.\n")
        return
    
    
    for num in range(0, stairs):
        print("@" + " " * num + '@')
        
        
def repeating_squares():
    #program repeating_squares receives no arguments
    #it prompts the user for the amount of squares to repeat
    #outputs in turtle
    
    squares = int(input("How many squares would you like? "))
    #input validation
    while squares < 1 :
        print("Please enter a valid entry for the amount of squares.\n")
        return
    
    
    t.speed(0)
    
    t.delay(0)
    
    #accumulator
    SQUARE_SIZE = 10
        
    for num in range(squares):
        for num1 in range(4):
            t.left(90)
            t.forward(SQUARE_SIZE)
            
        SQUARE_SIZE += 5
    t.done()
    
def hypnotic_pattern():
    #program hypnotic_pattern receives no inputs
    #it asks user for how many patterns they would like
    #displays a spiral square pattern with size set by user
    #shows result in turtle
    
    
    patterns = int(input("How many spirals would you like? "))
    while patterns < 1 :
        print("Please enter a valid entry for the amount of spirals.\n")
        return
    
    #accumulator
    spiral_modifier = 1
    
    #turtle setup
    t.delay(0)
    
    t.speed(0)
    t.left(90)
    t.forward(5)
    t.left(90)
    
    for num in range(patterns*4):
        t.forward(spiral_modifier + 10)
        t.left(90)
        spiral_modifier += 5
    t.done()
    