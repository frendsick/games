'''
Title:          Yatzy AI
Description:    AI for Yatzy game
Author:         Teemu Patsi
Date:           14th of November 2018
Version:        1.0.0
Python version: 2.7
Usage:          Import this file to yatzy.py
Notes:          This game is made as a final assignment for Data Structures and Algorithms course in JAMK University of Applied Sciences.

Change log:

2018:
        14th of November:
                1.0.1   Moved Player class to external file Player.py

'''
import time
from Player import Player

class Yatzy_AI(Player):
    
    name = 'Unnamed BOT'
    
    # Multiplications
    aces_weight             = 7
    twos_weight             = 5
    threes_weight           = 4
    fours_weight            = 4
    fives_weight            = 5
    sixes_weight            = 6
    
    pair_weight             = 8
    two_pair_weight         = 6
    three_of_a_kind_weight  = 8
    four_of_a_kind_weight   = 11
    small_straight_weight   = 3
    large_straight_weight   = 5
    full_house_weight       = 8
    chance_weight           = 1
    yatzhee_weight          = 1337

    def AI_Turn(AI_players, i):
            print("/nBOT {0}'s turn!\n".format(AI_players[i].name))
            AI_players[i].Print_Points()

            players[i].Choose(False)
            dices = [0,0,0,0,0]

	    # Returns dice values after players throws
            dices = Throws(dices)

            # AI evaluates where to put points
            pick = AI_players[i].Choose()
            
            AI_players[i].Update_Points(pick, dices)
            AI_players[i].Print_Points()

    @staticmethod
    def Evaluate_Throws(dices, chosen_dices, players, i):
        
        else:

        return dices, chosen_dices

    def Evaluate_final():
        return
