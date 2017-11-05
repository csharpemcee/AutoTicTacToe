# Tic-Tac-Toe - repeated games of AI VS. AI
# Used for a demonstration of machine learning. (reminds me of War Games)
# Copyright (c) 2017 Christopher Sacchi

# first value is column, second is row

import math

neural = neural2 = {}
table = {0: {0: 0, 1: 0, 2: 0}, 1: {0: 0, 1: 0, 2: 0}, 2: {0: 0, 1: 0, 2: 0}}
rules = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
scores = {0: 0, 1: 0}
done = False
i = a = 0

while True:
	while done == False:
#		rules (1 / 1 + math.exp(-rules[]))

		if (table[0][0] == 1 and table[1][1] == 1 and table[2][2] == 1) or (table[2][0] == 1 and table[1][1] == 1 and table[0][2] == 1) or (table[0][0] == 1 and table[1][0] == 1 and table[2][0] == 1) or (table[0][1] == 1 and table[1][1] == 1 and table[2][1] == 1) or (table[0][2] == 1 and table[1][2] == 1 and table[2][2] == 1) or (table[0][0] == 1 and table[0][1] == 1 and table[0][2] == 1) or (table[1][0] == 1 and table[1][1] == 1 and table[1][2] == 1) or (table[2][0] == 1 and table[2][1] == 1 and table[2][2] == 1):
			scores[0] += 1
			print("X WINS")
			break
		elif (table[0][0] == 2 and table[1][1] == 2 and table[2][2] == 2) or (table[2][0] == 2 and table[1][1] == 2 and table[0][2] == 2):
			scores[1] += 1
			print("O WINS")
			break

		done = True

		for i in range(3):
			for a in range(3):
				if table[i][a] == 0:
					done = False
			if i == 2 and done == True:
				print("DRAW") # what we should expect a lot more of at the very end
				break
		i = a = 0
	done = False
	table = {0: {0: 0, 1: 0, 2: 0}, 1: {0: 0, 1: 0, 2: 0}, 2: {0: 0, 1: 0, 2: 0}}
