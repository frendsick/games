'''
Title:          Yatzy
Description:    Yatzy game to play with friends
Author:         Teemu Patsi
Date:           13th of November 2018
Version:        1.0.1
Python version: 2.7
Usage:          Try it :)
Notes:			This game is made as a final assignment for Data Structures and Algorithms course in JAMK University of Applied Sciences.

Change log:

2018:
	13th of November:
		1.0.1	Moved Player class to external file Player.py
		
'''

from Player import Player
from yatzy_AI import Yatzy_AI
import random
# Self-made mergesort algorithm implementation
from mergesort import mergesort


# Calls for gameloop and asks for new game after game has ended
def main():
	while True:
		Yatzy()
		newGame = raw_input("New game (y/n)? ")
		if (newGame == 'n' or newGame == 'N'):
			break

# Generate player objects at the start of the game
def Instantiate_Players():
	players = []
	player_amount = raw_input("How many players? ")
	
	for i in range (0, int(player_amount)):
		name = raw_input("What is player {}'s name? ".format(i+1))
		p = Player(name)
		players.append(p)
	return players
	
# Gameloop
def Yatzy():

	# Make all players
	players = Instantiate_Players()
	game_over = False
	
	while not game_over:
		# Loops through all the players
		for i in range(0,len(players)):
			
			# Print only if there is 2 or more players
			if (len(players) > 1):
				print ("\n{}'s turn!\n".format(players[i].name))
				players[i].Print_Points()
			
			players[i].Choose(False)
			dices = [0,0,0,0,0]
			
			# Returns dice values after players throws
			dices = Throws(dices)
			
			# Player picks where to put points
			pick = players[i].Choose(True)
			
			players[i].Update_Points(pick, dices)
			players[i].Print_Points()
		
			# If last player has used all slots, game is over
			if len(players[len(players)-1].used) == 15:
				game_over = True
				print ("\nGame over!")
				Who_Won(players)
	
def Throws(dices):
	chosen_dices = []
	# Maximum of three throws
	for throw in range(0,3):
	
		# Throw 5 dices each time
		for i in range(0,5):
			if str(i+1) not in chosen_dices:
				dices[i] = random.randrange(1, 7)
		
		print ("\nThrow {0}: {1}".format(throw+1, dices))
		
		# Asks player what dices he/she chooses to keep
		if (throw < 2):
			dices, chosen_dices, is_ready = Which_Dices_To_Keep(dices, chosen_dices)
		
		# If player decides to keep all of dices as is break from the loop
		if (is_ready):
			break
	
	return dices
	
def Which_Dices_To_Keep(dices, chosen_dices):

	valid_input = False
	
	while not valid_input:
                # valid_input changes to False if wrong raw_input is inserted
                valid_input = True 
                chosen_dices = []
		keep = raw_input("Which dices you'd like to keep? ")
		
		# Iterate through all chars
		for i in range(0, len(keep)):
			if keep[i] != '1' and keep[i] != '2' and keep[i] != '3' and keep[i] != '4' and keep[i] != '5':
				valid_input = False
				break
			else:
				# Checks if user's input has some integer multiple times
				for j in range(0, len(chosen_dices)):
					if chosen_dices[j] == keep[i]:
						valid_input = False
						break
					
				chosen_dices.append(keep[i])
		
		# Tells player how to choose
		if (not valid_input):
			print ("Just insert numbers for dices. F.ex. '1235' will throw again dices 1,2,3 and 5")
	
	if (len(chosen_dices) >= 5):
		is_ready = True
	else:
		is_ready = False
	
	return dices, chosen_dices, is_ready
	
def Who_Won(players):
	# Sorts players list in descending point order
	mergesort(players)
	for i in range(0,len(players)):
		players[i].Print_Points()
	print ("\n{0} won with {1} points!\n".format(players[0].name, players[0].total))
	
if __name__ == "__main__":
	main()
