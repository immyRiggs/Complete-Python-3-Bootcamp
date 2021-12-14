# Milestone Priject 1: Tic Tac Toe
board_pos = [['1','2','3'],['4','5','6'],['7','8','9']]
board_now = []
for element in board_pos:
    for item in element:
        board_now.append(item)
print(board_now)

# Ask if player 1 is X or O
player_pieces = ['X','O']
player1 = "Q"
player2 = "R"
def define_players(player1,player2):
    player1 = "Q"
    player2 = "R"
    while player1 not in player_pieces:
        player1 = input('Player 1, choose "X" or "O": ')
        if player1 not in player_pieces:
            print('Please choose "X" or "O".')
    if player1 == 'X':
        player2 = 'O'
    else: 
        player2 = 'X'
#define_players(player1,player2)

# Display board with numbered locations and display current board state
board_pos = [['1','2','3'],['4','5','6'],['7','8','9']]
game_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def display_board(board):
        print('|'.join(board[0]))
        print('-----')
        print('|'.join(board[1]))
        print('-----')
        print('|'.join(board[2]))
        print('\n\n')
# display game
def display_game(board_pos,game_board):
    display_board(board_pos)
    display_board(game_board)

# Take input

# Check for winner

###############

# display winner, ask to play again