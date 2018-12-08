import sys

the_board = {1: ' 1 ', 2:' 2 ',3:' 3 ',
         4: ' 4 ', 5:' 5 ',6:' 6 ',
         7:' 7 ',8:' 8 ', 9:' 9 ' }

def printBoard(board):
    print('\n')
    print(board[1] + '|' + board[2]+ '|' + board[3])
    print('----------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('----------')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')
printBoard(the_board)

def winning_combination(board):
    if (board[1] == board[2] == board[3]) or (board[4] == board[5] == board[6])\
        or (board[7] == board[8] == board[9]) or (board[1] == board[4] == board[7])\
        or (board[2] == board[5] == board[8]) or (board[3] == board[6] == board[9])\
        or (board[1] == board[5] == board[9]) or (board[3] == board[5] == board[7]):
        print('Wygrałeś')
        sys.exit(0)


while True:
    def playerOne():
        try:
            playerOneMove = input('Gdzie postawić X?(podaj cyfre) ')
            if int(playerOneMove) in the_board.keys():
                if the_board[int(playerOneMove)] == ' X ' or the_board[int(playerOneMove)] == ' o ':
                    print('To miejsce jest zajęte.')
                    playerOne()
                else:
                    the_board[int(playerOneMove)] = ' X '
                    printBoard(the_board)
                    winning_combination(the_board)
            else:
                print('wybierz cyfre od 1 do 9')
                playerOne()
        except ValueError:
            print('tylko cyfry z tabeli!')
            playerOne()
    playerOne()

    def playerTwo():
        try:
            playerOneMove = input('Gdzie postawić o?(podaj cyfre) ')
            if int(playerOneMove) in the_board.keys():
                if the_board[int(playerOneMove)] == ' o ' or the_board[int(playerOneMove)] == ' X ':
                    print('To miejsce jest zajęte.')
                    playerTwo()
                else:
                    the_board[int(playerOneMove)] = ' o '
                    printBoard(the_board)
                    winning_combination(the_board)
            else:
                print('wybierz cyfre od 1 do 9')
                playerTwo()
        except ValueError:
            print('tylko cyfry z tabeli!')
            playerTwo()

    playerTwo()
