import random

print("Welcome to Tic Tac Toe Game")
print("___________________________")

playerisready = True
boards = [" " for _ in range(9)]
existing_number = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8}

def board():
    dash = "_____________"
    row1 = f"\t{boards[0]}|\t{boards[1]}|\t{boards[2]}\n{dash}"
    row2 = f"\t{boards[3]}|\t{boards[4]}|\t{boards[5]}\n{dash}"
    row3 = f"\t{boards[6]}|\t{boards[7]}|\t{boards[8]}"
    print(f"{row1}\n{row2}\n{row3}")


def is_position_available(position):
    return boards[position] == " "


def check_for_win(symbol):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if boards[combo[0]] == boards[combo[1]] == boards[combo[2]] == symbol:
            return True
    return False


def pc_player(available_positions):
    return random.choice(list(available_positions.keys()))


def player_symbol(player1sym):
    if player1sym == "o":
        return ("o", "x")
    else:
        return ("x", "o")


def player(position, player_sym):
    boards[position] = player_sym.upper()
    board()


withwhometoplay = input("Want to play against pc(P) or with friend(F)?(Type P or F):").lower()

while playerisready:
    boards = [" " for _ in range(9)]
    new_existing_number = existing_number.copy()
    player1symbol, player2symbol = player_symbol(input("player 1 choose symbol O or X : ").lower())
    board()

    for n in range(5):
        print(new_existing_number)
        while True:
            player1Position = int(input("Player 1 press the position number: "))
            if is_position_available(new_existing_number[player1Position]):
                player(new_existing_number[player1Position], player1symbol)
                del new_existing_number[player1Position]
                if check_for_win(player1symbol):
                    print("Player 1 wins!")
                    break
            else:
                print("Position already taken")
                continue
            break

        if len(new_existing_number) == 0 or check_for_win(player1symbol):
            break

        while True:
            if withwhometoplay == "p":
                player2Position = pc_player(new_existing_number)
                print(f"Computer chose position: {player2Position}")
            else:
                player2Position = int(input("Player 2 press the position number: "))

            if is_position_available(new_existing_number.get(player2Position, -1)):
                player(new_existing_number.get(player2Position), player2symbol)
                del new_existing_number[player2Position]
                if check_for_win(player2symbol):
                    print("Player 2 wins!" if withwhometoplay == "f" else "Computer wins!")
                    break
            else:
                print("Position already taken")
                continue
            break

        if check_for_win(player2symbol):
            break

    withwhometoplay = input("Want to play against pc(P) or with friend(F) or 'Q' for quit?(Type P or F or Q):").lower()
