"""
always include thought process for non-trivial problems:

must check both diagonals and all rows and columns for a win
computer plays randomly

"""


import random as R
from doctest import COMPARISON_FLAGS
from wsgiref.validate import check_input

grid = [[" "," "," "],[" "," "," "],[" "," "," "]]

def display():
    for row in grid:
        print(str(row)+ "\n")


def check_input():
    in_row = int(input("Enter the desired row: "))
    in_col = int(input("Enter the desired col: "))
    if 0 < in_row <=3 and 0< in_col <= 3:
        if grid[in_row-1][in_col-1] == " ":
            grid[in_row-1][in_col-1] = "X"
        else:
            print("Error: entered cell is occupied\n")
            check_input()
    else:
        print("Error: indices out of grid bounds\n")
        check_input()


def comp_play():
    print("Computer's turn:\n")
    in_row = R.randint(1,3)
    in_col = R.randint(1,3)
    if grid[in_row - 1][in_col - 1] == " ":
        grid[in_row - 1][in_col - 1] = "O"
    else:
        comp_play()


def check_win():
    done = False
    empty = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                empty += 1

    # Check the rows
    for row in range(0, 2):
        if grid[row][0] == grid[row][1] == grid[row][2] in {"X" ,"O"}:
            winner = grid[row][0]
            print("Player " + winner  + " won!")
            done =  True

    # Check the columns
    for col in range(0, 2):
        if grid[0][col] == grid[1][col] == grid[2][col] in {"X" ,"O"}:
            winner = grid[row][0]
            print("Player " + winner + " won!")
            done =  True

    # Check the diagnoals

    if grid[0][0] == grid[1][1] == grid[2][2] in {"X" ,"O"}:
        winner = grid[0][0]
        print("Player " + winner + " won!")
        done = True
    elif grid[0][2] == grid[1][1] == grid[2][0] in {"X" ,"O"}:
        winner = grid[0][2]
        print("Player " + winner + " won!")
        done = True
    elif empty == 0:
        print("It is a draw")
        done = True

    return done

#note: a win and a grid being empty are not mutually exclusive


print("Welcome to Tic-Tac-Toe game: ")
check_win()
display()
while(True):
    if check_win() == False:
        check_input()
        display()
        check_win()
    if check_win() == False:
        comp_play()
        display()
        check_win()
    else:
        print("Game done!")
        break


