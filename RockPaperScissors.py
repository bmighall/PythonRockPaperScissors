# Assignment 4
# El E 237
# Ben Mighall
# 9/18/2018

# Rock-Paper-Scissors game. Plays to 3 points. 

# Added "clear window" feature on line 48. Change that to "cls" instead of "clear" if you're on Windows; should work.
# Can't defend against screen/keyboard peeking or pressing the up key on the keyboard, though. Honor system, I guess.

import os

score1 = 0
score2 = 0
player1list = []
player2list = []
valid = False
player1choice = 0
player2choice = 0
round = 1

print("Welcome to Rock-Paper-Scissors!\n")
print("The rules are simple: each player will be prompted for a choice, then the winner will be chosen!")
print("Remember: rock beats scissors, scissors beats paper, and paper beats rock!\n")
print("----------------------------------------------------------------\n")

while(score1 != 3 and score2 != 3):
	print("ROUND",round,"start!\n")
	# player 1 decision
	valid = False
	while(valid == False):
		player1choice = input("Player 1: it's your turn! Enter 1 for ROCK, 2 for PAPER, or 3 for SCISSORS:")
		if(player1choice == '1' or player1choice == '2' or player1choice == '3'):
			valid = True
			# this next part essentially fixes an issue I was having where I was comparing ints not strings, but I'm too lazy to fix it line by line
			if(player1choice == '1'):
				player1choice = 1
			elif(player1choice == '2'):
				player1choice = 2
			elif(player1choice == '3'):
				player1choice = 3
		else:
			print("That is an invalid selection. Please try again.\n")
			
	valid = False
	
	#Clears window so second person can't see what you typed for your choice 
	os.system("clear") #Change this to "cls" if you are on Windows. Should work fine if you're on Mac or Linux. 
    
	# player 2 decision
	while(valid == False):
		player2choice = input("Player 2: it's your turn now! Enter 1 for ROCK, 2 for PAPER, or 3 for SCISSORS:")
		if(player2choice == '1' or player2choice == '2' or player2choice == '3'):
			valid = True
			# this next part essentially fixes an issue I was having where I was comparing ints not strings, but I'm too lazy to fix it line by line
			if(player2choice == '1'):
				player2choice = 1
			elif(player2choice == '2'):
				player2choice = 2
			elif(player2choice == '3'):
				player2choice = 3
		else:
			print("That is an invalid selection. Please try again.\n")
	
	print("")

	#storing player 1 choice in list
	if(player1choice == 1):
		player1list.append("ROCK")
	elif(player1choice == 2):
		player1list.append("PAPER")
	elif(player1choice == 3):
		player1list.append("SCISSORS")
		
	#storing player 2 choice in list
	if(player2choice == 1):
		player2list.append("ROCK")
	elif(player2choice == 2):
		player2list.append("PAPER")
	elif(player2choice == 3):
		player2list.append("SCISSORS")
	
	# decision tree
	if(player1choice == 1):
		print("Player 1 chose ROCK.")
		if(player2choice == 1): #P1: Rock, P2: Rock -> TIE
			print("Player 2 chose ROCK.")
			print("It's a TIE! Neither player wins a point.")
		elif(player2choice == 2): #P1: Rock, P2: Paper -> P2 wins
			print("Player 2 chose PAPER.")
			print("PAPER beats ROCK! Player 2 wins!")
			score2 += 1
		elif(player2choice == 3): #P1: Rock, P2: Scissors -> P1 wins
			print("Player 2 chose SCISSORS.")
			print("ROCK beats SCISSORS! Player 1 wins!")
			score1 += 1
	elif(player1choice == 2):
		print("Player 1 chose PAPER.")
		if(player2choice == 1): #P1: Paper, P2: Rock -> P1 wins
			print("Player 2 chose ROCK.")
			print("PAPER beats ROCK! Player 1 wins!")
			score1 += 1
		elif(player2choice == 2): #P1: Paper, P2: Paper -> TIE
			print("Player 2 chose PAPER.")
			print("It's a TIE! Neither player wins a point.")
		elif(player2choice == 3): #P1: Paper, P2: Scissors -> P2 wins
			print("Player 2 chose SCISSORS.")
			print("SCISSORS beats PAPER! Player 2 wins!")
			score2 += 1
	elif(player1choice == 3):
		print("Player 1 chose SCISSORS.")
		if(player2choice == 1): #P1: Scissors, P2: Rock -> P2 Wins
			print("Player 2 chose ROCK.")
			print("ROCK beats SCISSORS! Player 2 wins!")
			score2 += 1
		elif(player2choice == 2): #P1: Scissors, P2: Paper -> P1 wins
			print("Player 2 chose PAPER.")
			print("SCISSORS beats PAPER! Player 1 wins!")
			score1 += 1
		elif(player2choice == 3): #P1: Scissors, P2: Scissors -> TIE
			print("Player 2 chose SCISSORS.")
			print("It's a TIE! Neither player wins a point.")
			
	print("\nCurrent Scores:")
	print("Player 1:",score1)
	print("Player 2:",score2,"\n")
	round += 1

if score1 == 3:
	print("GAME OVER. CONGRATULATIONS PLAYER 1! YOU WIN!\n")
	print("Player 1 choices by round:")
	r = 0
	for x in player1list:
		r += 1
		print("Round",r,"-",x)
	print("\nPlayer 2 choices by round:")
	r = 0
	for x in player2list:
		r += 1
		print("Round",r,"-",x)
elif score2 == 3:
	print("GAME OVER. CONGRATULATIONS PLAYER 2! YOU WIN!\n")
	print("Player 1 choices by round:")
	r = 0
	for x in player1list:
		r += 1
		print("Round",r,"-",x)
	print("\nPlayer 2 choices by round:")
	r = 0
	for x in player2list:
		r += 1
		print("Round",r,"-",x)
