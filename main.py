import random

gameBoard = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
winner = None
player = "X"


# ------------------------------------------------------------------------------

# print the game board
def printingboard(gameBoard):
    print(gameBoard[0] + "|" + gameBoard[1] + "|" + gameBoard[2])
    print("-----------")
    print(gameBoard[3] + "|" + gameBoard[4] + "|" + gameBoard[5])
    print("----------")
    print(gameBoard[6] + "|" + gameBoard[7] + "|" + gameBoard[8])


# ------------------------------------------------------------------------------

# first player input
def playerinput(gameboard):
    inp = int(input("It's your turn please enter a number between 1-9"))
    if inp < 1 or inp > 9 or inp not in range(1, 10):
        print("please enter a valid number between 1-9")
        playerinput(gameBoard)
    if inp >= 1 and inp <= 9 and gameboard[inp - 1] == "-":
        gameboard[inp - 1] = player
    else:
        print("oops this spot is taken please choose another one ")
        playerinput(gameboard)


# ------------------------------------------------------------------------------


# check for win or tie
def checkwins(gameBoard):
    global winner
    if gameBoard[0] == gameBoard[1] == gameBoard[2] != "-":
        winner = gameBoard[0]
        return True
    elif gameBoard[3] == gameBoard[4] == gameBoard[5] != "-":
        winner = gameBoard[3]
        return True
    elif gameBoard[6] == gameBoard[7] == gameBoard[8] != "-":
        winner = gameBoard[6]
        return True
    elif gameBoard[0] == gameBoard[3] == gameBoard[6] != "-":
        winner = gameBoard[0]
        return True
    elif gameBoard[1] == gameBoard[4] == gameBoard[7] != "-":
        winner = gameBoard[1]
        return True
    elif gameBoard[2] == gameBoard[5] == gameBoard[8] != "-":
        winner = gameBoard[2]
        return True
    elif gameBoard[0] == gameBoard[4] == gameBoard[8] != "-":
        winner = gameBoard[0]
        return True
    elif gameBoard[2] == gameBoard[4] == gameBoard[6] != "-":
        winner = gameBoard[2]
        return True


def checktie(gameBoard):
    # global gameContinue
    if "-" not in gameBoard:
        printingboard(gameBoard)
        print("game Ended no winner ")
        exit()
        # gameContinue=False


def checkwinner(gameBoard):
    if checkwins(gameBoard):
        printingboard(gameBoard)
        print(f"Game Ended And WINNER Is <<< {winner} >>> .")
        exit()


# ------------------------------------------------------------------------------


# switch the player
def changeplayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


# ------------------------------------------------------------------------------

# uncomment this part of code to make second player the computer
# def computer_turn(gameBoard):
#     while player=="O":
#         position=random.randint(0,8)
#         if gameBoard[position]=="-":
#             gameBoard[position]="O"
#             changeplayer()

# ------------------------------------------------------------------------------

while (True):
    printingboard(gameBoard)
    playerinput(gameBoard)
    checkwinner(gameBoard)
    checktie(gameBoard)
    changeplayer()
    # computer_turn(gameBoard)
