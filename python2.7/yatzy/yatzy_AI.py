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
    def Evaluate_Throws(dices, chosen_dices, players, ind):
        time.sleep(0.4)
        while (True):
            # If five dices are the same
            if (dices[0] == dices[1] == dices[2] == dices[3] == dices[4]):
                if (not players[ind].used.contains('Yatzy') or not players[ind].used.contains('Four of a Kind') or not players[ind].used.contains('Three of a Kind') or (not players[ind].used.contains('Chance') and dices[0] > 4) or not players[ind].used.contains('Pair') and (dices.count(5) > 1 or dices.count(6) > 1)):
                    chosen_dices.append('1','2','3','4','5')
                    return dices, chosen_dices
                elif (dices[0] > 3 and (not players[ind].used.contains('Pair') or not players[ind].used.contains('Two Pair') or not players[ind].used.contains('Chance'))):
                    chosen_dices.append('1','2')
                    return dices, chosen_dices
                else:
                    break
            
            # Try if dices contains 4 of a kind or 3 of a kind
            for x in range(0, len(dices)):
                if (dices.count(dices[x]) >= 4):
                    chosen_dices = Yatzy_AI.Four(dices, players, ind, x)
                    return dices, chosen_dices
                elif (dices.count(dices[x]) >= 3):
                    chosen_dices = Yatzy_AI.Three(dices, players, ind, x)
                    return dices, chosen_dices
            
            break


        return dices, chosen_dices

    # Triggers if there is four dices with the same value 
    @staticmethod
    def Four(dices, players, ind, x):
        chosen_dices = []
        if ('Four of a Kind' not in players[ind].used or 'Three of a Kind' not in players[ind].used or 'Chance' not in players[ind].used and (sum(dices) / len(dices) > 3 ) or ('Pair' not in players[ind].used and (dices.count(5) > 1 or dices.count(6) > 1))):
            for i in range (0, len(dices)):
                if dices[i] == dices[x]:
                    chosen_dices.append(str(i+1))

            print chosen_dices
            return chosen_dices
    
    @staticmethod
    # Triggers if there is three dices with the same value 
    def Three(dices, players, ind, x):
        chosen_dices = []
        if ('Threes' not in players[ind].used or 'Three of a Kind' not in players[ind].used or ('Chance' not in players[ind].used and (sum(dices) / len(dices) > 3 )) or 'Fours' not in players[ind].used):
            for i in range(0, len(dices)):
                if dices[i] == dices[x]:
                    chosen_dices.append(str(i+1))
            return chosen_dices

        elif ('Full House' not in players[ind] or ((dices.count(5) > 1 or dices.count(6) > 1) and ('Pair' not in players[ind].used or 'Two Pair' not in players[ind].used or 'Chance' not in players[ind].used))):
            pair = 0
            for i in range(0, len(dices)):
                # Test if there is bigger pair available, then it is full house
                if ('Full House' not in players[ind].used and dices.count(dices[i]) > 1 and (best_pair != dices[i] and best_pair != 0)):
                    chosen_dices.append('1','2','3','4','5')
                    return chosen_dices
                if (dices.count(dices[i]) > 1 and (best_pair != dices[i] and best_pair != 0)):
                    best_pair = dices[i]
            for i in range(0, len(dices)):
                if pair == dices[i]:
                    chosen_dices.append(str(i+1))
            return chosen_dices 

        return chosen_dices

    def Evaluate_final():
        return
