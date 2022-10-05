import random

first_row = ["[ ]","[ ]","[ ]","[ ]","[ ]"]
second_row = ["[ ]","[ ]","[ ]","[ ]","[ ]"]
third_row = ["[ ]","[ ]","[ ]","[ ]","[ ]"]
fourth_row = ["[ ]","[ ]","[ ]","[ ]","[ ]"]
fifth_row = ["[ ]","[ ]","[ ]","[ ]","[ ]"]

print("      Wordle.py")
print("",*first_row,"\n",*second_row,"\n",*third_row,"\n",*fourth_row,"\n",*fifth_row)


#with these lines we generate a random int
#and use it to get a random answer for the wordle
answerfile = open("answers.txt",'r')
ansnum = random.randint(0, 316)
content = answerfile.readlines()
answer = content[ansnum]
answerfile.close()



guessfile = open("guesses.txt","r")

choice = input("Enter a guess (5 letter word): ")

#input val
good = True
while good:
    if len(choice) != 5:
        print("Your guess was not 5 letters long. Please try again.")
        
        choice = input("\nEnter a guess (5 letter word): ")
    else:
        good = False

