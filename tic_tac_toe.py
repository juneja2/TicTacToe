
import os

player1 = None
player2 = None
times = 1
player1_turn = True
input_list = [" "] * 10

def wanna_play():
    global player1
    global player2
    global times

    if times == 1:
        print("Welcome to Tic Tac Toe")
        player1 = ask_X_or_O_for_player1()
        player2 = set_player2(player1)
    else:
        switch_player_position()
         
    times += 1
    
    return valid_input()

def ask_X_or_O_for_player1():
    while True:
        player1 = input("Player 1: Do you want to be X or O\n").upper()
        if player1 in "OX":
            return player1

def set_player2(player1):
    if player1 == "X":
        return "O"

    return "X"

def switch_player_position():
    global player1
    global player2
    if player1 == "X":
        player1 = "O"
        player2 = "X"
    else:
        player1 = "X"
        player2 = "O"

def valid_input():
    while True:
        choice = input("Are you ready to play. Enter Yes or No\n").lower()
        if choice == "yes":
            print("Player 1 will go first")
            return True
        elif choice == "no":
            return False
        else:
            print("Please enter Yes or No")

def change_player_turn():
    global player1_turn
    if player1_turn:
        player1_turn = False
    else:
        player1_turn = True

def valid_input_pos():
    
    global input_list
    while True:
        input_pos = int(input("Choose your next position 1-9 "))
        if  input_pos in range(1, 10):
            if input_list[input_pos] != " ":
                print("Invalid position specified")
            elif player1_turn:
                input_list[input_pos] = player1
                return
            else:
                input_list[input_pos] = player2
                return
        else:
            print("Out of range position")

def display_board():

    component = {"empty": "     |     |     \n", "border":"-----------------\n", 0: "  {}  |  {}  |  {}  \n"}

    # Inserted " " in the place where there isn't a number
    
    #Now printing the tic tac toe with X and O's
    #In the format 
    # 7 8 9
    # 4 5 6
    # 1 2 3
    i = 7
    while i >= 1:
        print(component["empty"])
        print(component[0].format(input_list[i], input_list[i + 1], input_list[i + 2]))
        print(component["empty"])
        
        if i != 1:
            print(component["border"])
            
        i -= 3
        
def reset_input_list():
    global input_list
    
    input_list = [" "] * 10

def win():
    if not player1_turn:
        for i in range(1, 10, 3):
            if input_list[i] == input_list[i+1] == input_list[i + 2] == player1:
                return "p1"
        if input_list[1] == input_list[5] == input_list[9] == player1 or input_list[3] == input_list[5] == input_list[7] == player1:
            return "p1"
        return False
        
    else:
        for i in range(1, 10, 3):
            if input_list[i] == input_list[i+1] == input_list[i + 2] == player2:
                return "p2"
        if input_list[1] == input_list[5] == input_list[9] == player2 or input_list[3] == input_list[5] == input_list[7] == player2:
            return "p2"
        return False

def main_loop():
    total_inputs = 0
    while wanna_play():
        # WE need to keep track of the places where what has gone
        
        while total_inputs < 10:
            w = win()
            if type(w) != bool or total_inputs == 9:
                os.system("cls")
                break
            else:
                os.system("cls")
                
                display_board()
                
                valid_input_pos()
                
                total_inputs += 1
                change_player_turn()
        
        display_board()
        if win() == "p1":
            print("Player 1 wins")
        elif win() == "p2":
            print("Player 2 wins")
        else:
            print("It's a tie")
            
        reset_input_list()
        total_inputs = 0
        
main_loop()
