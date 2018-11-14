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

class Yatzy_AI():
    
    name = 'Unnamed'
    
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


    def __init__(self, name):
        self.name = name

        # For point evaluation purposes
        self.eval = 0


    def AI_Turn(AI_players):
        for i in range(0,len(AI_players):
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

    def Evaluate_Throws():
        return

    # Method for point evaluation for AI
    def Choose():
        if 'Aces' not in self.used:
            print ("1: Aces")
        if 'Twos' not in self.used:
            print ("2: Twos")
        if 'Threes' not in self.used:
            print ("3: Threes")
        if 'Fours' not in self.used:
            print ("4: Fours")
        if 'Fives' not in self.used:
            print ("5: Fives")
        if 'Sixes' not in self.used:
            print ("6: Sixes")
        if 'Pair' not in self.used:
            print ("7: Pair")
        if 'Two Pair' not in self.used:
            print ("8: Two Pair")
        if 'Three of a Kind' not in self.used:
            print ("9: Three of a Kind")
        if 'Four of a Kind' not in self.used:
            print ("10: Four of a Kind")
        if 'Small Straight' not in self.used:
            print ("11: Small Straight")
        if 'Large Straight' not in self.used:
            print ("12: Large Straight")
        if 'Full House' not in self.used:
            print ("13: Full House")
        if 'Chance' not in self.used:
            print ("14: Chance")
        if 'Yatzy' not in self.used:
            print ("15: Yatzy")

        time.sleep(0.7)
        
        # Evaluate where to put points
        Evaluate_final()

    def Evaluate_final():
        return
