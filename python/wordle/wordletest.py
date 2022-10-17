import random
from colorama import Fore, Style

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



#temp input#
answer = "cigar"
# ------------ input section ------------ #

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



#making sure word actually exists
exists = False
line = guessfile.readline()

while line != '':
    
    line = line.rstrip("\n")
    
    if line.lower() == choice.lower():
        exists = True
        
    line = guessfile.readline()
    
    

if not exists:
    print("Your word was not recognized as a correct input. Please try again.")
    
    
choicelist = [*choice]
anslist = [*answer]



print(anslist)

#checking if a common letter exists
commonletter = False

def itemchecker(list1,list2):
    
    itemlist = []
    
    for item in list1:
        
        if item in list2:
            
            commonletter = True
            itemlist.append(item)
            
            place_in_choice = list1.index(item)
            
            place_in_ans = list2.index(item)
            
    return itemlist, place_in_ans, place_in_choice

itemlist, place_in_ans, place_in_choice = itemchecker(choicelist,anslist)

print(itemlist)
        
if commonletter:
    if place_in_choice == place_in_ans:
        #common letter exists & is same placement
        sameplace = True
    else:
        #common letter exists but not the same placement
        sameplace = False
        

for amoung in range(5):
    
    #print(Fore.RED + <string>)
    #print(Style.RESET_ALL + <string>)
    
    if amoung == place_in_ans:
        first_row[amoung] = "\033[1;33;m" + "[" + choice[amoung] + "]"
        
    elif place_in_choice == place_in_ans:
        
        first_row[amoung] = str("\033[1;32;m" + "[" + choice[amoung] + "]")
        
    else:
        first_row[amoung] = "[" + choice[amoung] + "]"
    
print(*first_row)