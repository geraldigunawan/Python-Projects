#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 13:07:07 2019

@author: geraldigunawan
The Goal: Remember Adventure? Well, we’re going to build a more basic version of that.
 A complete text game, the program will let users move through rooms based on user input 
 and get descriptions of each room. To create this, you’ll need to establish the directions 
 in which the user can move, a way to track how far the user has moved (and therefore which
 room he/she is in), and to print out a description. You’ll also need to set limits for how 
 far the user can move. In other words, create “walls” around the rooms that tell the user, 
 “You can’t move further in this direction.”

"""
from Player import Player
from pprint import pprint
#%% Story line

valid_directions = ["left","up","down","right"]
board_rows = 10
board_columns = 10

def create_board():
    board = [[0]*board_rows for _ in range(board_columns)]
    return board
    
def showGameIntro(index):
    switcher = {
        0: "You are inside a small building. You discover that this is a one room house with four walls.There is debris spread over the entire floor and it is obvious that there hasn’t been anyone here for a long time. Over in the corner there is a large open thropy case. there is a large sofa covering most of the floor. There is a large gas lamp. You need to get out of that house in 5 steps before a vampire eats you.",
        1: "You are in story 2",
        2: "You are in story 3",
        3: "You are in story 4",
    }
    return switcher.get(index, lambda: "nothing")
        
def showStoryline(row_index, column_index):
    return False
    
def checkOutOfBounds(player, direction):
    positionX = getPlayerPosition(player)[0]
    positionY = getPlayerPosition(player)[1]
    if (direction == "left"):
        positionX = positionX;
        positionY = positionY - 1;  
    if (direction == "right"):
        positionX = positionX;
        positionY = positionY + 1;  
    if (direction == "up"):
        positionX = positionX - 1;
        positionY = positionY;    
    if (direction == "down"):
        positionX = positionX + 1;
        positionY = positionY;
    if (positionX >= board_rows or positionX < 0 or positionY >= board_columns or positionY < 0):
        return True
    return False
        
def setPlayerPosition(board,player, direction):
    if (direction == "left"):
        player.x = player.x;
        player.y = player.y - 1;  
    if (direction == "right"):
        player.x = player.x;
        player.y = player.y + 1;  
    if (direction == "up"):
        player.x = player.x - 1;
        player.y = player.y;    
    if (direction == "down"):
        player.x = player.x + 1;
        player.y = player.y;
    board[player.x][player.y] = 1
    
def getPlayerPosition(a):
    return (a.x, a.y)
    
def checkUserInput(a):
    a = a.lower();
    while(a[0:3] != "go "):
        a = input("not valid answer. What would you like to do?")
        a = a.lower();
    a = checkDirection(a)
    return a

def checkDirection(b):
    b.lower();
    while (b[3:] not in valid_directions):
        b = input("direction not found. What would you like to do?")
        b = b.lower()
        b = checkUserInput(b)
    return b
#%%
playgame = input("Play game? (y/n): ")

while (playgame == "y"): 
    #initialize game and player
    player_life = 10
    room  = create_board()
    player = Player()
    room[getPlayerPosition(player)[0]][getPlayerPosition(player)[1]] = 1
    print(showGameIntro(0));
    pprint(room)
    print("Step left: ", player_life)
    
    #game in progress
    while (player_life >= 0):
        userInput = input("What would you like to do?")
        direction = checkUserInput(userInput)[3:]
        #print ("direction requested is ", direction)
        while(checkOutOfBounds(player, direction) == True):
            pprint(room)
            print("Step left: ", player_life)
            userInput = input("That's a wall. Enter again: ")
            direction = checkUserInput(userInput)[3:]
        setPlayerPosition(room,player,direction)
        #print(getPlayerPosition(player));
        pprint(room)
        player_life -= 1
        if (player_life > -1):
            print("Step left: ", player_life)
        else: print("Game over")
    playgame = "n"
    playgame = input("You have been eaten by vampire. Play again? (y/n)")
print("Bye bye")