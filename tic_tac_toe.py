import os
import time

def set_player2(player1):
    return "O" if player1 == "X" else "X"

def get_players():
    player1 = None
    while True:
        player1 = input("Player 1: Do you want to be X or O ").upper()
        if player1 == "O" or player1 == "X":
            break
        else:
            print("Invalid symbol for player1")
        
    player2 = set_player2(player1)
    return player1, player2

def wanna_play():
    choice = None
    while True:
        choice = input("Do you want to play? Enter Yes or No ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid answer")
    
def display_board(input_list):
    components = {"empty": "     |     |     ", "border":"-----------------", 0: "  {}  |  {}  |  {}  "}

    for i in range(7, 0, -3):
        print(components["empty"])
        print(components[0].format(input_list[i], input_list[i + 1], input_list[i + 2]))
        print(components["empty"])

        if i != 1:
            print(components["border"])
def get_num_input(input_list, player1, player2, player1_turn):
    while True:
        num = int(input("Please enter a number between 1-9 "))
        if num in range(1, 10):
            if input_list[num] == " ":
                input_list[num] = player1 if player1_turn else player2
                return input_list
            else:
                print("Position already filled")
        else:
            print("Number out of range")

def change_player_turn(player1_turn):
    return not player1_turn

def switch_player_symbols(player1):
    if player1 == "X":
        return ("O", "X")
    return ("X", "O")
def someone_won(input_list, player1, player2):

    for i in range(0, 3):
        j = 3 * i
        equal1 = input_list[j + 1] == input_list[j + 2] == input_list[j + 3]
        equal2 = input_list[i + 1] == input_list[i + 4] == input_list[i + 7]
        
        if equal1:
            if input_list[j + 1] == player1:
                return player1
            elif input_list[j + 1] == player2:
                return player2
        elif equal2:
            if input_list[i + 1] == player1:
                return player1
            elif input_list[i + 1] == player2:
                return player2

        
    first_check = input_list[1] == input_list[5] == input_list[9]
    second_check = input_list[3] == input_list[5] == input_list[7]

    if first_check or second_check:
        if input_list[5] == player1:
            return player1
        elif input_list[5] == player2:
            return player2  

    return False
        # Returning False if nobody wons
        # Returning player if somebody wins

def main_loop():
    input_list = [" "] * 10
    player1 = None
    player2 = None
    player1_turn = True
    
    print("Welcome to Tic Tac Toe")
    player1, player2 = get_players()

    while wanna_play():
        if player1_turn:
            print("Player1'{}' goes first".format(player1))
        else:
            print("Player2'{}' goes first".format(player2))
        time.sleep(2)
        total_inputs = 0
        
            
        while total_inputs < 9:
            winner = someone_won(input_list, player1, player2)
            os.system("cls")
            if winner ==  False:
                # Checking winner == False because it also possible that someone_won return a string
                display_board(input_list)
                # Our updated input_list and change_player_turn
                input_list = get_num_input(input_list, player1, player2, player1_turn)
                player1_turn = change_player_turn(player1_turn)

                os.system("cls")
                total_inputs += 1
            else:
                #We will only come here if we have a winner
                break
        winner = someone_won(input_list, player1, player2)
        
        display_board(input_list)
        if winner == False:
            #This means we have a tie
            print("It's a tie")
        elif winner == player1:
            print("Player1 wins")
        else:
            print("Player2 wins")
        player1, player2 = switch_player_symbols(player1)
        input_list = [" "] * 10
        # Resetting the input list
        


main_loop()
