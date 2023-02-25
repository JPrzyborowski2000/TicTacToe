import numpy as np

game = [[1,1,2],
		[0,2,1],
		[2,2,0],]

diags = []
for ix in range(len(game)):
	diags.append(game[ix][ix])

for col, row, in zip(reversed(range(len(game))), range(len(game))):
	print(col,row)
	diags.append(game[row][col])

print(diags)

'''
for col in range(len(game)):
	check = []

	for row in game:
		check.append(row[col])

	if check.count(check[0]) == len(check) and row[0] != 0:
		print("Winner !")



def win(current_game):
	for row in game:
		print(row)
		if row.count(row[0]) == len(row) and row[0] != 0:
			print("Winner !")

win(game)

game = [[0,0,0],
		[0,0,0],
		[0,0,0],]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		print("   0  1  2")
		if not just_display:
			game_map[row][column] = player
		for count,row in enumerate(game):
			print(count,row)
	except IndexError as e:
		print("Error: Did you input row/column as 0 1 or 2?",e)
	
	except Exception as e:
		print("Something go wrong !")
		
	return game_map

game = game_board(game, player=1, row=2, column=1)
''' 