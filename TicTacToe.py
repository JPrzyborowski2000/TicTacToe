import itertools

def win(current_game):
	#Horizontal
	for row in game:	
		if row.count(row[0]) == len(row) and row[0] != 0:
			print(f"Player {row[0]} is the winner horizontally.")

	#Diagonal
	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		print(f"Player{diags[0]} is the winner diagonally (\\).")

	diags = []
	for col, row, in zip(reversed(range(len(game))), range(len(game))):
		diags.append(game[row][col])
	
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		print(f"Player{diags[0]} is the winner diagonally(/).")

	#Vertical
	for col in range(len(game)):
		check = []

		for row in game:
			check.append(row[col])

		if check.count(check[0]) == len(check) and row[0] != 0:
			print(f"Player{check[0]} is the winner vartically")


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

Play = True
players = [1,2]
while Play:
	game = [[0,0,0],
			[0,0,0],
			[0,0,0],]

	game_won = False
	game = game_board(game, just_display=True)
	while not game_won:
		current_player = 1
		column_chocie = int(input("What column do you want play? (0, 1, 2):"))
		row_chocie = int(input("What row do you want play? (0, 1, 2):"))
		game = game_board(game,current_player,row_chocie,column_chocie)


#game = game_board(game, player=1, row=2, column=1)
