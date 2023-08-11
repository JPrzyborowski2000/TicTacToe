game_size = 3

'''
print("   0  1  2")
s = "   "+"  ".join([str(i) for i in range(game_size)])
print(s)
'''

'''
for i in range(game_size):
	row = []
	for i in range(game_size):
		row.append(0)
	game.append(row)
'''

game = [[0 for i in range(game_size)] for i in range(game_size)]
print(game)
