from random import randrange

available_board = [1, 2, 3, 4, 6, 7, 8, 9]
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
game_over = False

def player_turn(available_board, board):
    while True:
        a = int(input('Your move: '))
        if a not in available_board:
            print('Move not available.')
            continue
        else:
            break
    for i in available_board:
        if i == a:
            available_board.remove(i)
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == a:
                board[i][j] = 'O'
    return available_board, board


def computer_turn(available_board, board):
    while True:
        b_rand = randrange(len(available_board))
        b = available_board[b_rand]
        print(b)
        if b == 'X':
            continue
        else:
            break
    for i in available_board:
        if i == b:
            available_board.remove(i)
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == b:
                board[i][j] = 'X'
    return available_board, board


def display_board(board):
    for i in range(3):
        print(('+' + '-' * 7) * 3 + '+')
        print(('|' + ' ' * 7) * 3 + '|')
        print(('|' + ' ' * 3 + str(board[i][0]) + ' ' * 3) + '|' + ' '*3 + str(board[i][1]) + ' '*3 + '|' + ' '*3 + str(board[i][2]) + ' '*3 + '|')
        print(('|' + ' ' * 7) * 3 + '|')
    print(('+' + '-'*7)*3+ '+')

def check_winner(available_board, board):
    global game_over
    #3 Os horizontally, vertically, diagonally then player win
    for i in range(3):
        if board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O':
            print('You won!')
            display_board(board)
            game_over = True
            return
        elif board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
            print('You won!')
            display_board(board)
            game_over = True
            return
        elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            print('You won!')
            display_board(board)
            game_over = True
            return
        elif board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
            print('You lost...')
            display_board(board)
            game_over = True
            return
        elif board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
            print('You lost...')
            display_board(board)
            game_over = True
            return
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        print('You won!')
        display_board(board)
        game_over = True
        return
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        print('You lost...')
        display_board(board)
        game_over = True
        return
    elif len(available_board) == 0:
        print('We drew.')
        display_board(board)
        game_over = True
        return

while game_over == False:
    display_board(board)
    player_turn(available_board, board)
    check_winner(available_board, board)
    computer_turn(available_board, board)
    check_winner(available_board, board)
