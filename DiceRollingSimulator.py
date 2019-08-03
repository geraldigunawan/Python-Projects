# -*- coding: utf-8 -*-

"""
The Goal: Like the title suggests, this project involves writing a program 
that simulates rolling dice. When the program runs, it will randomly choose a 
number between 1 and 6. (Or whatever other integer you prefer — 
the number of sides on the die is up to you.) The program will print what that number is. 
It should then ask you if you’d like to roll again. For this project, you’ll need to set 
the min and max number that your dice can produce. For the average die, that means a minimum of 1 
and a maximum of 6. After dice is rolled, the user needs to guess what that number is. 
(In other words, the user needs to be able to input information.) 
If the user’s guess is wrong, the program should return some sort of indication as to how wrong 
(e.g. The number is too high or too low). If the user guesses correctly, a positive indication 
should appear"""

import random

#%%
valid_yes_answers = ["y", "yes", "yeah", "ya"]
valid_no_answers = ["no", "nah", "n", "np", "nope"]
valid_guess_answers = ['1', '2', '3', '4', '5', '6']
valid_answers = valid_yes_answers + valid_no_answers + valid_guess_answers

def rollDice():
    random_number = random.randint(1,6)
    #print ("actual number is ", random_number)
    return random_number

def checkNumber(guess_number, actual_number):
    if (guess_number < actual_number):
        print ("your number is a bit low");
    elif (guess_number > actual_number):
        print ("your number is a bit high");
    else:
        return 0
    
def checkInput(a):
    a = a.lower();
    while (a not in valid_answers):
        print ("Not valid answer")
        a = input("Enter again:");
    return a
#%%
answer = input("Would you like play roll a dice? (Y/N)");
answer = checkInput(answer);

while(answer in valid_yes_answers):
    player_life = 3
    actual_number = rollDice();
    print ("Dice is rolled!")
    while (player_life > 0):
        guess_answer = input("Please guess between 1 to 6?");
        guess_answer = checkInput(guess_answer);
        result = checkNumber(int(guess_answer),int(actual_number))
        if (result == 0):
            print ("your guess is right! Congratulations, you win!")
            break;
        player_life -= 1
    if (player_life == 0):
        print ("You've run out of lives. You lose.")
    answer = input("Would you like to play again? (Y/N)");
    answer = checkInput(answer)
        
print ("Thanks, bye-bye");
#%%
                