import turtle as t
import time

def day_converter():
    #program day_converter receives no arguments
    #asks user for a number in range 1 through 7 from monday to sunday
    #displays the corresponding day of the week in spanish
    #also checks if the user entered anything outside of 1-7
    #uses if-elif-else statements
    
    day = int(input("Enter a number between 1 and 7: "))
    
    if day == 1:
        print("Lunes")
    elif day == 2:
        print("Martes")
    elif day == 3:
        print("Miércoles")
    elif day == 4:
        print("Jueves")
    elif day == 5:
        print("Viernes")
    elif day == 6:
        print("Sábado")
    elif day == 7:
        print("Domingo")
    else:
        print("This number is out of range. Try again.")
        day_converter()

def roman_numerals():
    #program roman_numerals receives no arguments
    #asks user to enter a number from 1 to 10
    #program displays the roman numeral version of that number
    #also makes sure no out of range numbers are entered
    
    number = int(input("Enter a number between 1 and 10: "))
                 
    if number == 1:
        print("I")
    elif number == 2:
        print("II")
    elif number == 3:
        print("III")
    elif number == 4:
        print("IV")
    elif number == 5:
        print("V")
    elif number == 6:
        print("VI")
    elif number == 7:
        print("VII")
    elif number == 8:
        print("VIII")
    elif number == 9:
        print("IX")
    elif number == 10:
        print("X")
    else:
        print("This number is out of range. Try again.")
        roman_numerals()
        
def color_mixer():
    #program color_mixer receives no arguments
    #asks user for two primary colors to mix
    #uses three stored color values: red, blue, and yellow
    #combines the two that user selects and prints it
    
    firstcolor = input("Enter a primary color (red, blue, yellow): ")
    secondcolor = input("Enter another primary color (red, blue, yellow): ")
    
    colormix = firstcolor.lower() + secondcolor.lower()
    
    if colormix == 'redblue' or colormix == 'bluered':
        print("When your colors mix, they become purple.")
    elif colormix == 'redyellow' or colormix == 'yellowred':
        print("When your colors mix, they become orange.")
    elif colormix == 'blueyellow' or colormix == 'yellowblue':
        print("When your colors mix, they become green.")
    elif firstcolor == secondcolor:
        print("It... it makes",firstcolor + "...")
    else:
        print("You did not enter correct colors. Please try again.")
        color_mixer()

def hot_dog():
    #program hot_dog receives no arguments
    #asks user for how many people are attending and how many hotdogs each person will eat
    #calculates how many hotdog packages required, how many bun packages required,
    #number of hotdogs left over, and number of buns left over
    
    DOGS_PER_PACKAGE = 10
    BUNS_PER_PACKAGE = 8
    
    people = int(input("How many people will be attending your event? "))
    dogsperperson = int(input("How many hotdogs will be served per person? "))
    
    totaldogs = people * dogsperperson

    
    dogsrequired = totaldogs / DOGS_PER_PACKAGE
    bunsrequired = totaldogs / BUNS_PER_PACKAGE
    
    
    dogs_left = dogsrequired % 8
    buns_left = bunsrequired % 10
    print(dogs_left)
    print(buns_left)
    
    if not(dogs_left.is_integer()):
        dogsrequired = int(dogsrequired) + 1
        if not(buns_left.is_integer()):
            bunsrequired = int(bunsrequired) + 1
    elif not(buns_left.is_integer()):
        bunsrequired = int(bunsrequired) + 1
    
    
        
        
    bunsleftover = (bunsrequired * 8) - totaldogs
    dogsleftover = (dogsrequired * 10) - totaldogs
    
    print("The minimum packages of hotdogs you will need is:",dogsrequired)
    print("The minimum packages of dog buns you will need is:",bunsrequired)
    print("The number of hot dogs left over is:",dogsleftover)
    print("The number of dog buns left over is:",bunsleftover)
    

def time_calculator():
    #program time_calculator receives no arguments
    #asks user for an amount of seconds
    #if seconds is above 60 then program will convert it to minutes and seconds
    #if seconds is above 3600 then program will convert it to hours, minutes, and seconds
    #if seconds is above 86400 then program will convert it to days, hours, minutes, and seconds
    #prints result
    
    seconds = int(input("Enter an amount of seconds:"))
    
    if seconds >= 86400:
        days = seconds // 86400
        hours = (seconds - (days*86400)) // 3600
        minutes = ((seconds - (days * 86400)) - (hours * 3600)) // 60
        seconds = (((seconds - (days * 86400)) - (hours * 3600)) - (minutes * 60))
        print("Your input equals:",days,"day(s),",hours,"hour(s),",minutes,"minute(s) and",seconds,"second(s).")
    elif seconds >= 3600:
        hours = seconds // 3600
        minutes = (seconds - (hours * 3600)) // 60
        seconds = ((seconds - (hours * 3600)) - (minutes * 60))
        print("Your input equals:",hours,"hour(s),",minutes,"minute(s) and",seconds,"seconds.")
    elif seconds >= 60:
        minutes = seconds // 60
        seconds = seconds - (minutes * 60)
        print("Your input equals:",minutes,"minute(s) and",seconds,"second(s).")
    elif seconds <= 0:
        print("Bad answer. You have been BANNED!")
        return
    else:
        print("Your input equals:",seconds,"second(s).")
    
    
def leap_year():
    #program leap_year receives no arguments
    #asks user to input a certain year
    #calculates if that year is a leap year
    #if so, tells user his choice is a leap year
    
    
    year = float(input("Please enter a year: "))
    
    year_calc = year / 100
    
    year_calc2 = year / 400
    
    year_calc3 = year / 4
    
    if year_calc.is_integer():
        if year_calc2.is_integer():
            print(int(year),"is a leap year. There are 29 days in February.")
        else:
            print(int(year),"is not a leap year. There are 28 days in February.")
    elif year_calc3.is_integer():
        print(int(year),"is a leap year. There are 29 days in February.")
        
    else:
        print(int(year),"is not a leap year. There are 28 days in February.")
        
def sir_fix_alot():
    
    print("First, try and reboot your computer and try to connect.")
    print("")
    
    computer_reboot = input("Did that work? ")
    
        
    if computer_reboot.lower() == 'y' or computer_reboot.lower() == 'yes':
        print("Netflix and Chill")
    elif computer_reboot.lower() == 'n' or computer_reboot.lower() == 'no':
        print("Alright, now restart the router and try to connect.")
        print("")
        router_reboot = input("Did that work? ")
        
        if router_reboot.lower() == 'yes' or router_reboot.lower() == 'y':
            print("Netflix and Chill")
        elif router_reboot.lower() == 'no' or router_reboot.lower() == 'n':
            print("If that did not work, verify that all of the cables are connected correctly.")
            print("")
            verify_cables = input("Did that work? ")
            
            if verify_cables.lower() == 'yes' or verify_cables.lower() == 'y':
                print("Netflix and Chill")
            elif verify_cables.lower() == 'no' or verify_cables.lower() == 'n':
                print("Ok, instead try and move the router to a better location.")
                print("")
                move_router = input("Did that work? ")
                
                if move_router.lower() == 'yes' or move_router.lower() == 'y':
                    print("Netflix and Chill")
                elif move_router.lower() == 'no' or move_router.lower() == 'n':
                    print("Alright, then you should get a new router buddy.")
                    return
                
                else:
                    print("Your answer was not correct. Please try again.")
                    return
            
        else:
            print("Your answer was not correct. Please try again.")
            return
    else:
        print("Your answer was not correct. Please try again.")
        return
        
def can_we_just_eat():
    #program can_we_just_eat receives no arguments
    #it asks the user if the group he is going to eat with is vegan, vegetarian, or
    #gluten-free
    #then uses a list of restaurants with pre-set conditions including if they support
    #those options
    #prints the options allowed for the group
    
    vegetarians = input("Is anyone in your party a vegetarian? (yes/no) ")
    vegans = input("Is anyone in your party a vegan? (yes/no) ")
    glutenfrees = input("Is anyone in your party gluten-free? (yes/no) ")
    
    if vegetarians.lower() == 'yes':
        vegetarians = True
    elif vegetarians.lower() == 'no':
        vegetarians = False
    
    if vegans.lower() == 'yes':
        vegans = True
    elif vegans.lower() == 'no':
        vegans = False
        
    if glutenfrees.lower() == 'yes':
        glutenfrees = True
    elif glutenfrees.lower() == 'no':
        glutenfrees = False
    
    answer = [vegetarians,vegans,glutenfrees]
    print(answer)
    if answer == [False, False, False]:
        print("Your choices are: ")
        print("")
        print("Joe’s Gourmet Burgers\nMain Street Pizza Company\nCorner Café\nMama’s Fine Italian\nThe Chef’s Kitchen")
    elif answer == [True, False, False]:
        print("Your choices are: ")
        print("")
        print("Main Street Pizza Company\nCorner Café\nMama’s Fine Italian\nThe Chef’s Kitchen")
    elif answer == [False, True, False]:
        print("Your choices are: ")
        print("")
        print("Corner Café\nThe Chef’s Kitchen")
    elif answer == [False, False, True]:
        print("Your choices are: ")
        print("")
        print("Main Street Pizza Company\nCorner Café")
    elif answer == [True, False, True]:
        print("Your choices are: ")
        print("")
        print("Main Street Pizza Company\nCorner Café\nThe Chef’s Kitchen")
    elif answer == [False, True, True]:
        print("Your choices are: ")
        print("")
        print("Corner Café\nThe Chef’s Kitchen")
    elif answer == [True, True, True]:
        print("Your choices are:")
        print("")
        print("Corner Café\nThe Chef’s Kitchen")
    else:
        print("Your answer was not yes or no for one of your answers. Please try again.")
        can_we_just_eat()

def hit_the_target():
    #program hit_the_target takes no arguments
    #turtle creates a box with preset constants
    #user is asked to enter power and angle of launch for arrow
    #then displays it on turtle
    
    
    #constant setting
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    TARGET_LLEFT_X = 100
    TARGET_LLEFT_Y = 250
    TARGET_WIDTH = 25
    FORCE_FACTOR = 30
    PROJECTILE_SPEED = 1
    NORTH = 90
    SOUTH = 270
    EAST = 0
    WEST = 180
    
    
    #turtle setup
    t.clearscreen()
    t.screensize(SCREEN_WIDTH,SCREEN_HEIGHT)
    t.speed(0)
    
    
    #box creation
    normalwidth = t.width()
    t.width(TARGET_WIDTH)
    t.up()
    t.goto(TARGET_LLEFT_X,TARGET_LLEFT_Y)
    t.down()
    t.goto(TARGET_LLEFT_X,TARGET_LLEFT_Y)
    t.forward(25)
    t.seth(SOUTH)
    t.forward(25)
    t.seth(WEST)
    t.forward(25)
    t.seth(NORTH)
    t.forward(25)
    
    
    #resetting turtle for user
    
    t.up()
    t.goto(0,0)
    t.down()
    t.speed(PROJECTILE_SPEED)
    t.width(normalwidth)
    
    
    #asking user for inputs
    
    angle = int(input("Enter the angle at which to launch: "))
    power = int(input("Enter the power at which to launch: "))
    
    
    #running of user inputs
    
    t.seth(angle)
    t.forward(FORCE_FACTOR * power)
    
    
    #if statement checking if turtle is within target
    
    if t.xcor() >= 100 and t.xcor() <= 125 and t.ycor() >= 225 and t.ycor() <= 250:
        print("You hit the target!")
        time.sleep(5)
        return
    else:
        print("You did not hit the target.")
        if angle < 60:
            print("Try going with more of an angle.")
        elif angle > 70:
            print("Try using less angle.")
        if power < 8:
            print("You should also try using more power.")
        elif power > 9:
            print("Your power is too strong! Try less power as well.")
        
