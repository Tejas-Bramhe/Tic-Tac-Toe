import random

print("WELCOME TO GAME: TIC TAC TOE")

def print_board(grid):
    for i in range(1, 10, 3):
        print(f" {grid[i]} | {grid[i+1]} | {grid[i+2]} ")
        if i < 7:
            print("---|---|---")

def winner_detect(grid, symbol):
    win_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]
    for combinations in win_combinations:
        if all(grid[position]==symbol for position in combinations):
            return True
    return False

grid = [' ' for _ in range(10)]
print_board(grid)

# Player chooses a symbol
player_symbol = input("Choose your symbol (X or O): ").upper()
while player_symbol not in ['X', 'O']:
    player_symbol = input("Invalid choice. Choose X or O: ").upper()

if player_symbol == 'X' :
    computer_symbol = 'O'
else :
    computer_symbol = 'X'

print(f"You are {player_symbol}, Computer is {computer_symbol}\n")
#game is starting with player's move
for turn in range(9):                                                             # Maximum 9 turns ,turn =0 to turn =9
    if turn % 2 == 0:                                                                           # Player's turn
        move = int(input("Enter your move (1-9): "))
        while move < 1 or move > 9 or grid[move] != ' ':
            move = int(input("Invalid move. Enter again (1-9): "))
        grid[move] = player_symbol
    else:                                                                                      # Computer's turn
        move = random.choice([i for i in range(1, 10) if grid[i] == ' '])
        grid[move] = computer_symbol
        print(f"Computer chooses position {move}")

    print_board(grid)

   
    if turn >= 4:                                                                  # Minimum turns required for a win is 5
        if winner_detect(grid, player_symbol):
            print("Congratulations! You win!")
            break
        elif winner_detect(grid, computer_symbol):
            print("Computer wins! Better luck next time.")
            break
else:
    print("It's a draw!")
