# make board of 3*3
# ask user to put x or o for one by one
# 2 player or play with pc
# put x o one by one
# all the area is full then anounce draw win or loss
# ask if u like to continue to play or quit

print("Welcome to Tic Tac Toe Game")
print("___________________________")

playerisready = True
score = 0


def scoreboard(score):
    score += 1


def board():
    dash = "_____________"
    board = ["" for n in range(9)]
    row1 = f"\t{board[0]}|\t{board[1]}|\t{board[2]}\n{dash}"
    row2 = f"\t{board[3]}|\t{board[4]}|\t{board[5]}\n{dash}"
    row3 = f"\t{board[6]}|\t{board[7]}|\t{board[8]}"
    print(f"{row1}\n{row2}\n{row3}")


def pcplayer():
    pass


def player(player1, player2):
    player1=0


withwhometoplay = input("Want to play against pc(P) or with friend(F)?(Type P or F):").lower()

while playerisready:
    if withwhometoplay == "p" or withwhometoplay == "f":
        board()
        print("where you want to mark")
        player1 = int(input("Player 1 press the position number: "))

        scoreboard(score)
    elif withwhometoplay == "q":
        playerisready = False
    else:
        print("You entered wrong character please use the 'P' or 'F' or 'Q'\n")
    withwhometoplay = input("Want to play against pc(P) or with friend(F) or 'Q' for quit?(Type P or F):").lower()
