'''
Title:          Player class
Description:    Class for Yatzy game
Author:         Teemu Patsi
Date:           13th of November 2018
Version:        1.1.1
Python version: 3.6
Usage:          * Keep this file and empty __init__.py in same repository as yatzy.py
				* Must have 'from Player import Player' line at the beginning of yatzy.py
Notes:			This file is part of yatzy.py file. This game is my a final assignment for Data Structures and Algorithms course in JAMK University of Applied Sciences.

Change log:

2018:
	13th of November:
		1.1.0   Moved Player class to this external file. Updated comments and author notes

'''

class Player:
	
	name = 'Unnamed'
	
	def __init__(self, name):
		self.used = []

		# Different points
		self.aces 				= 0
		self.twos 				= 0
		self.threes 			= 0
		self.fours 				= 0
		self.fives				= 0
		self.sixes				= 0
		self.bonus 				= 0
		self.upper_total 		= 0
		
		self.pair				= 0
		self.two_pair 			= 0
		self.three_of_a_kind	= 0
		self.four_of_a_kind 	= 0
		self.small_straight 	= 0
		self.large_straight 	= 0
		self.full_house 		= 0
		self.chance 			= 0
		self.yatzhee 			= 0
		
		self.total				= 0
		
		# Player's name is 'Unnamed' if empty string is provided
		if name != '':
			self.name = name
	
	def Choose(self, throw_done):
		
		# For checking
		empty_points = []
		
		if 'Aces' not in self.used:
			print ("1: Aces")
			empty_points.append('1')
		if 'Twos' not in self.used:
			print ("2: Twos")
			empty_points.append('2')
		if 'Threes' not in self.used:
			print ("3: Threes")
			empty_points.append('3')
		if 'Fours' not in self.used:
			print ("4: Fours")
			empty_points.append('4')
		if 'Fives' not in self.used:
			print ("5: Fives")
			empty_points.append('5')
		if 'Sixes' not in self.used:
			print ("6: Sixes")
			empty_points.append('6')
		if 'Pair' not in self.used:
			print ("7: Pair")
			empty_points.append('7')
		if 'Two Pair' not in self.used:
			print ("8: Two Pair")
			empty_points.append('8')
		if 'Three of a Kind' not in self.used:
			print ("9: Three of a Kind")
			empty_points.append('9')
		if 'Four of a Kind' not in self.used:
			print ("10: Four of a Kind")
			empty_points.append('10')
		if 'Small Straight' not in self.used:
			print ("11: Small Straight")
			empty_points.append('11')
		if 'Large Straight' not in self.used:
			print ("12: Large Straight")
			empty_points.append('12')
		if 'Full House' not in self.used:
			print ("13: Full House")
			empty_points.append('13')
		if 'Chance' not in self.used:
			print ("14: Chance")
			empty_points.append('14')
		if 'Yatzy' not in self.used:
			print ("15: Yatzy")
			empty_points.append('15')
		
		put_points = ''
		
		# I wanted that the code above can be showed without throwing
		if throw_done:
			while True:
				put_points = raw_input("\nWHERE TO PUT YOUR POINTS? ")
				if put_points in empty_points:
					break
	                        	
		return put_points
		
	def Update_Points(self, put_points, dices):
		if put_points == '1':
			self.Update_Aces(dices)
		elif put_points == '2':
			self.Update_Twos(dices)
		elif put_points == '3':
			self.Update_Threes(dices)
		elif put_points == '4':
			self.Update_Fours(dices)
		elif put_points == '5':
			self.Update_Fives(dices)
		elif put_points == '6':
			self.Update_Sixes(dices)
		elif put_points == '7':
			self.Update_Pair(dices)
		elif put_points == '8':
			self.Update_Two_Pair(dices)
		elif put_points == '9':
			self.Update_Three_of_a_Kind(dices)
		elif put_points == '10':
			self.Update_Four_of_a_Kind(dices)
		elif put_points == '11':
			self.Update_Small_Straight(dices)
		elif put_points == '12':
			self.Update_Large_Straight(dices)
		elif put_points == '13':
			self.Update_Full_House(dices)
		elif put_points == '14':
			self.Update_Chance(dices)
		elif put_points == '15':
			self.Update_Yatzhee(dices)
		
		if self.upper_total >= 63 and self.bonus == 0:
			print ("Bonus yey!")
			self.bonus += 50
			self.total += 50

	def Update_Aces(self, dices):
		self.used.append('Aces')
		for i in range(0,len(dices)):
			if dices[i] == 1:
				self.aces += 1
				self.upper_total += 1
				self.total += 1
	
	def Update_Twos(self, dices):
		self.used.append('Twos')
		for i in range(0,len(dices)):
			if dices[i-1] == 2:
				self.aces += 2
				self.upper_total += 2
				self.total += 2
				
	def Update_Threes(self, dices):
		self.used.append('Threes')
		for i in range(0,len(dices)):
			if dices[i] == 3:
				self.aces += 3
				self.upper_total += 3
				self.total += 3
				
	def Update_Fours(self, dices):
		self.used.append('Fours')
		for i in range(0,len(dices)):
			if dices[i] == 4:
				self.aces += 4
				self.upper_total += 4
				self.total += 4
	
	def Update_Fives(self, dices):
		self.used.append('Fives')
		for i in range(0,len(dices)):
			if dices[i] == 5:
				self.aces += 5
				self.upper_total += 5
				self.total += 5
	
	def Update_Sixes(self, dices):
		self.used.append('Sixes')
		for i in range(0,len(dices)):
			if dices[i] == 6:
				self.aces += 6
				self.upper_total += 6
				self.total += 6
	
	def Update_Pair(self, dices):
		self.used.append('Pair')
		for i in range(0,len(dices)):
			# Test if there is multiple occurrences of this number and if there is bigger pair available
			if (dices.count(dices[i]) > 1 and 2*dices[i] > self.pair):
				self.pair += 2*dices[i]
				self.total += 2*dices[i]
	
	def Update_Two_Pair(self, dices):
		self.used.append('Two Pair')
		pair_num = 0
		pair_cnt = 0
		for i in range(0,len(dices)):
		
			# If there is one pair and it's not the same we already acknowledged
			if (dices.count(dices[i]) > 1 and pair_num != dices[i]):
				pair_num += dices[i]
				pair_cnt += 1
			
			# If there was two separate pairs
			if (pair_cnt > 1):
				self.two_pair += 2*pair_num
				self.total += 2*pair_num
				break
	
	def Update_Three_of_a_Kind(self, dices):
		self.used.append('Three of a Kind')
		for i in range(0,len(dices)):
			if (dices.count(dices[i]) >= 3):
				self.three_of_a_kind += 3*dices[i]
				self.total += 3*dices[i]
				break
	
	def Update_Four_of_a_Kind(self, dices):
		self.used.append('Four of a Kind')
		for i in range(0,len(dices)):
			if (dices.count(dices[i]) >= 4):
				self.three_of_a_kind += 4*dices[i]
				self.total += 4*dices[i]
				break
		
	# Values from 1 to 5
	def Update_Small_Straight(self, dices):
		self.used.append('Small Straight')
		if (1 in dices and 2 in dices and 3 in dices and 4 in dices and 5 in dices):
			self.small_straight += 15
			self.total += 15
		
	# Values from 2 to 6
	def Update_Large_Straight(self, dices):
		self.used.append('Large Straight')
		if (2 in dices and 3 in dices and 4 in dices and 5 in dices and 6 in dices):
			self.small_straight += 20
			self.total += 20
			
	# 3 of a kind and a pair	
	def Update_Full_House(self, dices):
		self.used.append('Full House')
		first_number = 0
		second_number = 0
		cnt1 = 0
		cnt2 = 0

		for i in range(0, len(dices)):
			if second_number == 0 and first_number != 0 and first_number != dices[i]:
				second_number = dices[i]
				cnt2 += 1
				
			elif first_number == 0:
				first_number = dices[i]
				cnt1 += 1
				
			elif dices[i] == first_number:
				cnt1 += 1
			elif dices[i] == second_number:
				cnt2 +=1
				
		if (cnt1 == 3 and cnt2 == 2) or (cnt1 == 2 and cnt2 ==3):
			self.full_house += sum(dices)
			self.total += sum(dices)
		
	def Update_Chance(self, dices):
		self.used.append('Chance')
		
		# Every dice counts
		for i in range(0,len(dices)):
			self.chance += dices[i]
			self.total += dices[i]
		
	def Update_Yatzhee(self, dices):
		self.used.append('Yatzy')
		
		# All dices are equal
		if dices[0] == dices[1] == dices[2] == dices[3] == dices[4]:
			self.yatzhee += 50
			self.total += 50
	
	def Print_Points(self):
		print ("{0} has {1} points".format(self.name, self.total))
		# Prints if player does not have enough points from aces to sixes and game is not over
		if self.bonus == 0 and len(self.used) < 15:
			print ("Upper total is {0}".format(self.upper_total))
		
	
