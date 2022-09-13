# This program plays a modified game of 'craps'
# Name: Lauren Smillie
# Teacher: Mr. Rogers
# Created on 11/10/2020

import random

# Function will generate 2 random numbers from 1-6, and find the sum
def roll():
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    sum=die1+die2
    return sum
    
# Function will determine if the user's original POINT has a positive/negative score value
def points(a):
    if a == 11 or a == 7:
        return a
    elif a == 2 or a == 3 or a == 12:
        return 0-a
    else:
        return 0
    
# Function will calculate user's score
def score(a,b,c):
    rolls=[]
    if a!=0:
        total=a+b

    else:
        sum2=0
        while True:
            sum2=roll()
            rolls.append(sum2)
            if sum2==c or sum2==7:
                sum3=sum2
                break
        
        if sum3==7:
            total=b-7
        
        else:
            total=b+c
    return total,rolls

# Function will create a list of the user's rolls
def rollList(a,b):
    list=b
    list.insert(0,a)
    return list
    
# Function will print the user's rolls and score
def info(x,y):
    print("YOUR ROLLS:",x)
    print("SCORE:", y)

# Function will calculate if user won/lost
def winLose(a):
    if a>=60:
        print("You win!")
        
    elif a<=0:
        print("You lose :(")
    
    else:
        print("Bye for now!")

# Function will determine if user wants to continue/play again
def choice(a):
    if a.lower()=="y":
        return(True)
    
    else:
        return(False)

# Main program logic
playAgain=True
while (playAgain):
    total=20
    counter=0
    print("SCORE: 20")
    
    while total<60 and total>0 and (playAgain):
        # Store user's original POINT
        roll1=roll()
        
        # Store user's list of extra rolls and score
        result=score(points(roll1),total,roll1)
        total=result[0]
        
        # Print list of rolls and new score
        info(rollList(roll1,result[1]),total)
        
        # Calculate number of rolls
        if points(roll1) != 0:
            counter=counter+1

        else:
            counter=counter+len(rollList(roll1,result[1]))-1 
        
        # Ask if user wants to continue
        if total<60 and total>0:
            choice1=input("Continue? (y/n) ")
            playAgain=choice(choice1)
    
    # Print result of the game (win/lose)
    (winLose(total))
    
    # Print number of rolls
    print("You rolled the dice", counter, "times!")
    
    # Ask if user wants to play again
    choice2=input("Do you want to play again? (y/n) ")
    playAgain=choice(choice2)
    