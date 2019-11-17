from random import * # i import the random method with my function wheel_result()
from math import ceil # i import the method ceil of module math for my function compare()

def wheel_result():
    """i create a function for choose a random number"""
    wheel = randrange(0, 50)
    return wheel # i return the result of my function

def wheel_color(wheel): #
    """i create a function for verify is the number is pair or impair"""
    if wheel%2 ==0:
        # i declare the boolean True
        wheelColor = True
        return wheelColor # i return if the number  is pair
    elif wheel %2 != 0:
        # i declare the boolean False
        wheelColor = False
        return wheelColor # i return if the number is impair

def number_choice():
    """ i create a function for save the player number choice"""
    enter = 0
    # loops while enter is equality zero
    while enter == 0:
        playerNumber = input("enter a number enter 0 and 50:")
         # i use try for test the entry player
        try:
            float(playerNumber)
            enter = 1
             # i stop the loops if the player entry is a float or integer number
            break
        # i place the exept value error if the enttry is a string and display a message with print
        except ValueError:
            print("enter only number!!!")
    playerNumber = int(playerNumber)
    return playerNumber # i return this number

def color_choice(playerNumber): # i create a function with parametre to definite is the number player is pair or impair
    """i create a function with parametre to definite is the number player is pair or impair """
    if playerNumber %2 == 0:
        # i declare the boolean True
        playerColor = True
        return playerColor # i return if the number  is pair
    elif playerNumber %2 != 0:
        # i declare the boolean False
        playerColor = False
        return playerColor # i return if the number is impair

def compare(gain, bet, playerNumber, playerColor, wheel, wheelColor): # i create a function for compare the number and calculate the gain of player
    """i create a function for compare the number and calculate the gain of player"""
    if wheel == playerNumber:
        print("you win")
        # i multply the bet for 3 and adding result to gain
        gain = gain + (bet*3)
        # i round gain
        gain = ceil(gain)
        return gain

    elif wheelColor == playerColor:
        #i divide the bet for two and add result to gain
        gain = gain + (bet/2)
        # i round gain
        gain = ceil(gain)
        print("you win with same color")
        return gain
    else:# else i took of bet of gain
        gain = gain - bet
        # i round gain
        gain = ceil(gain)
        print("you loose")
        return gain
