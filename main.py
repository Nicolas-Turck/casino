from functions import * # i import all function of files functions.py
from random import * # i import the method random for random choice wheel
from math import ceil # i import the method ceil of math module to round the bet and the gain

print("welcome to the casino")
gain = 1000 # i declare the gain of departure is 1000$

while 1 :
    print("welcome to vegas $$")

    while gain > 0:
        #i throw a loop while the gain of player is tallest zero"""
        print("your gains {}$".format(gain))
        enter = 0
        #loops while enter is equality zero """
        while enter == 0:
            bet = input("your bet :")
            #i use try for test the entry player """
            try:
                float(bet) # float for player entry is float or integer
                enter = 1
                 # i stop the loops if the player entry is a float or integer number
                break
            # i place the exept value erro if the enttry is a string and display a message with print
            except ValueError:
                print("enter only number!!!")
         # i declare a variable is a egual the return of fonction
        wheel = wheel_result()
        # i declare a variable is a egual the return of fonction
        playerNumber = number_choice()
        # i display the the random number with the method format in the print
        print("the ball fall on .... {}".format(wheel))
         # i declare a variable is equal the return of function with parametre
        playerColor = color_choice(playerNumber)
        wheelColor = wheel_color(wheel)
        # i declare bet players is a float or integer
        bet = float(bet)
        # i declare the last variable with function to return the gain calculated of user
        gain = compare(gain, bet, playerNumber, playerColor, wheel, wheelColor)
        print("your gain {}$".format(gain))



    exit()        
